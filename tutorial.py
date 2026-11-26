from fastapi import FastAPI
from enum import StrEnum
from pydantic import BaseModel

class ModelName(StrEnum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/signup")
async def signup():
    return {"message": "Signed up"}

@app.put("/login")
async def login():
    return {"message": "Logged In"}

@app.get("/users")
async def get_all_users():
    return ["Ada", "Raphael", "Michael"]

@app.get("/users/me")
async def read_user_me():
    return {"message": "Current user"}

@app.get("/users/{userid}")
async def read_user_id(userid: int):
    return {"Here you go": userid}

@app.delete("/login")
async def del_user():
    return {"message": "Deleted"}

@app.get("/models/{model_name}")
async def get_model_name(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {
            "model name": model_name,
            "message": "Deep Learning FTW"
        }
    
    elif model_name == ModelName.lenet:
        return {
            "model name": model_name,
            "message": "LeCNN all the images"
        }

    return {
        "model name": model_name,
        "message": "Have some residuals"
    }

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file path": file_path}

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/items/{item_id}")
async def read_item_id(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"Description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}