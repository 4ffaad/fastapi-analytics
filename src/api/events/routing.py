from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema


router = APIRouter()

# List View
@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [
            {"id":1},{"id":2},{"id":3}
            ],
            "count": 3
        }

# Send data
# Create View 
@router.post("/")
def create_events(data:dict = {}) -> EventSchema:
    print(data)
    return { "id" : 123}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id":event_id}


#Update this data
@router.put("/{event_id}")
def update_event(event_id: int, payload:dict={}) -> EventSchema:
    return {"id":event_id}