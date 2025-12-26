from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"}


inventory = {1: {"name": "Item_1", "price": 10.0},
2: {"name": "Item_2", "price": 20.0},
3: {"name": "Item_3", "price": 30.0}}   

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description = "The ID of the item you want to retrieve", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item_by_name(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Error": "Item not found"}


@app.get("/search")
def search(name: Optional[str] = None, price: Optional[float] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name and inventory[item_id]["price"] == price:
            return inventory[item_id]
    return {"Error": "Item not found"}