import os
import redis
 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore
from decouple import config
from .fetch_data import product_metadata
 

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY') 

texts = [
    v['item_name'] for k, v in product_metadata.items()
]
 

metadatas = list(product_metadata.values())
 

embedding = OpenAIEmbeddings()
 

index_name = "products"


redis_url = config('REDIS_URL')
r = redis.Redis.from_url(redis_url, password=config('REDIS_PASSWORD'), socket_timeout=5, socket_keepalive=True)


vectorstore = RedisVectorStore.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=embedding,
    index_name=index_name,
    redis_url = redis_url
)