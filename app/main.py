from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI




app = FastAPI()


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}