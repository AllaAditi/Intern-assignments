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
    return {"billing":datas}


def create_item(item: Item):  # post
    billing.insert_one(item.dict())
    # db[item.id] = item.name
    return {
        "item succesfully added"
    }


def update_item(item_id: int, item: Item):  # put
    billing.update_one({"id": item_id}, {"$set": item.dict()})


def delete_item(item_id: int):
    billing.delete_one({"id": item_id})
    return {"message": "deleted"}


def pipeline_aggregation(pipeline: list):
    return billing.aggregate(pipeline)
