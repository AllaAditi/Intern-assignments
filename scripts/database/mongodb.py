from http import client

from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient  # import mongo client make connections to MongoDb
from scripts.constants.app_constants import DBConf

MONGO_URI = DBConf.MONGO_URI
app = FastAPI()

# Creating instance of mongo client
client = MongoClient(MONGO_URI)
# Creating database
db = client.interns_b2_23
# # Creating document
billing = db.aditi_biling


# It is our DataBase


# creating class
class Item(BaseModel):
    id: int
    name: str
    quantity: int
    cost: int


def read_item():  # get
    item = billing.find({})
    datas = []
    for items in item:
        data = {'id': items['id'], 'name': items['name'], 'quantity': items['quantity'], 'cost': items['cost']}
        datas.append(data)
    return {"billing": datas}


def create_item(item: Item):  # post
    billing.insert_one(item.dict())
    try:
        existing_item = billing.insert_one({"id": item.id})

        if existing_item:
            raise Exception(" ID already exists")

        billing.insert_one(item.dict())
        return {"message": "item created successfully"}

    except Exception as e:
        return {"message": str(e)}
    return {
        "item succesfully added"
    }


# def update_item(item_id: int, item: Item):  # put
# billing.update_one({"id": item_id}, {"$set": item.dict()})

def update_item(item_id: int, item: Item):
    try:
        billing.update_one({"id": item_id}, {"$set": item.dict()})
        return {"message": "Item updated"}
    except:
        return {"message": "Error updating item"}


def delete_item(item_id: int):
    try:
        billing.delete_one({"id": item_id})
        return {"message": "already deleted"}
    except:
        return {"message": "Item not found in the database"}


def pipeline_aggregation(pipeline: list):
    return billing.aggregate(pipeline)
