from fastapi import FastAPI
from routers import places
from routers import ai

app = FastAPI(title="Cheonha Yujeok API")

app.include_router(places.router, prefix="/places", tags=["places"])


@app.get("/")
def root():
    return {"message": "Cheonha Yujeok API is running"}

app.include_router(ai.router, prefix="/ai", tags=["AI"])