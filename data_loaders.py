from langchain.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatAnthropic
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from decouple import config
import os

CLAUDE_API_KEY = config('CLAUDE_API_KEY')

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')


file_path='./product_data/ProductsCollection.json'
data = json.loads(Path(file_path).read_text())

# pprint(data)
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
split_json = python_splitter.create_documents([json.dumps(data)])
# pprint(split_json)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(split_json, embeddings)
print(vectorstore)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectorstore.as_retriever(), memory=memory)

query = "What is the price of 'Non-Alcoholic Concentrated Perfume Oil'?"
result = qa({"question": query})

print(result['answer'])
