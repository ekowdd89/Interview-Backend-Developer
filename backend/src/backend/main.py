from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import engine

from . import models, routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(routes.router, prefix="/api/v1", tags=["Products"])

@app.get("/")
async def root():
    return {"message": "Hello World"}