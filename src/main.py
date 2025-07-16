from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from api.db.session import init_db
from api.events import router as events_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before app startup
    init_db()
    yield
    # Cleanup code if needed

app = FastAPI(lifespan=lifespan)  # <-- pass lifespan here

app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "Worlder"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
