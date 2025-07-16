import os
from fastapi import APIRouter, Depends
from sqlmodel import Session

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
@router.get("/")
def read_events() -> EventListSchema:
    print(os.getenv("DATABASE_URL"),DATABASE_URL)
    return {
        "results": [
            {"id":1},{"id":2},{"id":3}
            ],
            "count": 3
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


@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    return {"id":event_id}


#Update this data
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventModel:
    data = payload.model_dump()
    return {"id":event_id, **data}