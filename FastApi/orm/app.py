import uvicorn
from fastapi import FastAPI, HTTPException, status

from orm import Inventory
from db import Database

app = FastAPI()

db = Database()
inventory = Inventory(db)

@app.get("/inventory")
def list_inventory():
    return inventory.get_all_items()

@app.post("/inventory", status_code=status.HTTP_201_CREATED)
def add_inventory(item: dict):
    # new_item=inventory.add_item(name=item['name'],
    #                             qty=item['qty'],
    #                             buying_price=item['buying_price'], selling_price=item['selling_price'])
    #verification
    if not item.get('name'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item name is required")
    new_item = inventory.add_item(**item)
    return {"message": "Item added successfully", "item": new_item}

    if __name__=="__main__":
        uvicorn.run(app, port=8000)