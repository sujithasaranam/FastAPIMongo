from fastapi import APIRouter
from models.order_details import OrderDetail
from config.database import order_details_db
from serializers.serializer import list_order_detail_objects
from pymongo import ReturnDocument
from bson import ObjectId

router = APIRouter()

#GET Request Method
@router.get("/")
async def get_order_details():
    order_details = list_order_detail_objects(order_details_db.find())
    return order_details

#POST Request Method
@router.post("/")
async def post_order_details(order_detail: OrderDetail):
    order_details_db.insert_one(dict(order_detail))

#PUT Request Method
@router.put("/{id}")
async def put_order_details(id: str, order_detail: OrderDetail):
    order_details_db.find_one_and_update({"_id": ObjectId(id)}, {'$set': order_detail})

# #Patch Request Method
# @router.patch("/{id}")
# async def patch_order_details(id: str, order_detail: OrderDetail):
#     update_data = { "$set": order_detail.model_dump() }
#     updated_order = order_details_db.find_one_and_update({"_id": ObjectId(id)},  update_data, return_document=ReturnDocument.AFTER)
#     return updated_order

#Delete Request Method
@router.delete("/{id}")
async def delete_order_detail(id: str):
    order_details_db.find_one_and_delete({"_id": ObjectId(id)})
