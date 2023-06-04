import anthropic
from decouple import config
import shopify
import json
from pymongo.mongo_client import MongoClient
from decouple import config

shop_url = config('SHOP_URL')
api_key = config('API_KEY')
api_password = config('API_PASSWORD')
private_app_password = config('PRIVATE_APP_PASSWORD')
api_version = config('API_VERSION')

# MongoDB credentials
mongo_connection_string = config('MONGO_CONNECTION_STRING')
mongo_database = config('MONGO_DATABASE')
mongo_collection = config('MONGO_COLLECTION')


# shopify.Session.setup(api_key=api_key, secret=api_password)
# session = shopify.Session(shop_url, api_version, private_app_password)
# shopify.ShopifyResource.activate_session(session)


# Create a new client and connect to the server
# client = MongoClient(mongo_connection_string)
# db = client[mongo_database]
# collection = db[mongo_collection]

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# products = shopify.Product.find(limit=10)

# product_json_list = []
# for product in products:
#     product_json = product.to_dict()
#     product_json_list.append(product_json)

# product_json_string = json.dumps(product_json_list)
# print(product_json_string)

# Insert products into MongoDB
# collection.insert_many(product_json_list)