from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import SQLModel, Field
import sqlmodel 
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now


"""
id 
path 
description
"""

# page visits at any given time

class EventModel (TimescaleModel, table=True):
    page: str = Field(
        index=True
        )
    description: Optional[str] = ""

    updated_at: datetime = Field(
        default_factory=get_utc_now, 
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False)

    __chunk_time_interval__ = "INTERVAL 1 day"  
    __drop_after__ = "INTERVAL 3 months"

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")


class EventUpdateSchema(SQLModel):
    description: str


class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int