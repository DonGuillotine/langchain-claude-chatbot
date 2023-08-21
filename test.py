import anthropic
from pymongo.mongo_client import MongoClient
from decouple import config


API_KEY = config('CLAUDE_API_KEY')

# MongoDB credentials
mongo_connection_string = config('MONGO_CONNECTION_STRING')
mongo_database = config('MONGO_DATABASE')
mongo_collection = config('MONGO_COLLECTION')


# Create a new client and connect to the server
client = MongoClient(mongo_connection_string)
db = client[mongo_database]
collection = db[mongo_collection]


# Query products data 
all_products = collection.find() 
products_list = []
for product in all_products:
    products_list.append(product)

# print(products_list)


# anthropic_client = anthropic.Client(API_KEY)
# prompt = f"{anthropic.HUMAN_PROMPT}: You are a Smart customer Support chatbot, Here are a list of my products:\n\n{all_products}\n\n{anthropic.AI_PROMPT}: I have taken note of them, how may I be of assistance?\n\n{anthropic.HUMAN_PROMPT}:What is the price of '12 Ti Xelium Skis'?\n\n{anthropic.AI_PROMPT}\n\n"
# res = anthropic_client.completion(prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000)
# print(res)

print(products_list)
