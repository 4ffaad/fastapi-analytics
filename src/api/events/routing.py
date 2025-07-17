import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.db.session import get_session
from .models import (
    EventModel,
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)
from api.db.config import DATABASE_URL

router = APIRouter()

# List View
@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
    results = session.exec(query).all()
    return {
        "results": results,
        "count": len(results)       
    }

# Send data
# Create View 
@router.post("/", response_model=EventModel)
def create_events(
    payload:EventCreateSchema,
    session: Session = Depends(get_session)):

    # Validate and create the event object
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.get("/{event_id}", response_model=EventModel)
def get_event(
    event_id: int, 
    session: Session = Depends(get_session)
    ):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Event with id {event_id} not found."
        )
    return result


#Update this data
@router.put("/{event_id}", response_model=EventModel)
def update_event(
    event_id: int, 
    payload: EventUpdateSchema,
    session: Session = Depends(get_session)
):
    event = session.exec(select(EventModel).where(EventModel.id == event_id)).first()
    if not event:
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found.")

    data = payload.model_dump()
    for key, value in data.items():
        setattr(event, key, value)
        

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

# Delete this data  
@router.delete("/{event_id}", status_code=204)
def delete_event(
    event_id: int,
    session: Session = Depends(get_session)
):
    event = session.exec(select(EventModel).where(EventModel.id == event_id)).first()
    if not event:
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found.")

    session.delete(event)
    session.commit()
    return None  # 204 No Content