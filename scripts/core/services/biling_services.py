from fastapi import APIRouter
from scripts.schema.models import Item
from scripts.handler.biling_handler import ItemHandler
from scripts.handler.mail_handler import send_email, Email
from scripts.constants.app_constants import APis

item_router = APIRouter()


@item_router.get(APis.view_all_items_api)
def view_all_items():
    item_object = ItemHandler()
    return item_object.read_data()


@item_router.post(APis.create_api)
def create_item(item: Item):
    item_object = ItemHandler()
    return item_object.create_data(item)


@item_router.put(APis.update_api)
def update_item(item_id: int, item: Item):
    item_object = ItemHandler()
    return item_object.update_data(item_id, item)


@item_router.delete(APis.delete_api)
def delete_item(item_id: int):
    item_object = ItemHandler()
    return item_object.delete_data(item_id)


@item_router.post(APis.send_email)
def send_item(email: Email):
    item_handler = ItemHandler()
    result = item_handler.pipeline_aggregation()
    message = f"total amount is {result}"
    send_email(message, email)
    return {"message": "email sent"}


@item_router.get(APis.get_api)
def get_billing():
    item_handler = ItemHandler()
    return item_handler.pipeline_aggregation()
