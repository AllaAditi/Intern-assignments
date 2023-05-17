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
    data = []
    for items in billing.find():
        del items['_id']
        data.append(items)
    return {
        "db": data
    }


def create_item(item: Item):  # post
    billing.insert_one(item.dict())
    db[item.id] = item.name
    return {
        "db": db
    }


def update_item(item_id: int, item: Item):  # put
    billing.update_one({"id": item_id}, {"$set": item.dict()})


def delete_item(item_id: int):
    billing.delete_one({"id": item_id})
    return {"message": "deleted"}


def pipeline_aggregation(pipeline: list):
    return billing.aggregate(pipeline)
