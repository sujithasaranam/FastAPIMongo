from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

db_password = os.getenv('db_password')

client = MongoClient(f"mongodb+srv://admin:{db_password}@orderdetails.rnoyb.mongodb.net/?retryWrites=true&w=majority&appName=OrderDetails")

db = client.order_details

order_details_db = db['order_details']
