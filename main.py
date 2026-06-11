from fastapi import FastAPI
from routers import places, ai, wiki

app = FastAPI(title="Cheonha Yujeok API")

app.include_router(places.router, prefix="/places", tags=["places"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
app.include_router(wiki.router, prefix="/wiki", tags=["Wikipedia"])


@app.get("/")
def root():
    return {"message": "Cheonha Yujeok API is running"}