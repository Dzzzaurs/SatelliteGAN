from fastapi import FastAPI, Query
from pydantic import BaseModel

class ImageRequest(BaseModel):
    seed: str
    landscape: str