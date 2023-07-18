from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import (
    ConversationalRetrievalChain,
    LLMChain
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_models import ChatAnthropic
from langchain.prompts.prompt import PromptTemplate
from db.redis_vdb import vectorstore
from fine_tuning import RedisProductRetriever
from decouple import config


template = """Given the following chat history and a follow up question, rephrase the follow up input question to be a standalone question.
Or end the conversation if it seems like it's done.
Chat History:\"""
{chat_history}
\"""
Follow Up Input: \"""
{question}
\"""
Standalone question:"""
 
condense_question_prompt = PromptTemplate.from_template(template)
 
template = """You are a friendly, conversational ecommerce shopping assistant. Use the following context including product names, descriptions, and keywords to show the shopper whats available, help find what they want, and answer any questions.
It's ok if you don't know the answer.


Context:

{context}


\"""

Question:
\"""


Helpful Answer:"""

 
# qa_prompt= PromptTemplate.from_template(template)
qa_prompt = HumanMessagePromptTemplate.from_template(template)


llm = OpenAI(temperature=0)


streaming_llm = ChatAnthropic(
    anthropic_api_key=config('CLAUDE_API_KEY'),
    model="claude-v1.3-100k",
    streaming=True,  
    callback_manager=CallbackManager([
        StreamingStdOutCallbackHandler()
    ]),
    verbose=True,
)
 

question_generator = LLMChain(
    llm=llm,
    prompt=condense_question_prompt
)
 

chat_prompt = ChatPromptTemplate.from_messages([qa_prompt])


doc_chain = load_qa_chain(
    llm=streaming_llm,
    chain_type="stuff",
    prompt=chat_prompt
)

redis_product_retriever = RedisProductRetriever(vectorstore=vectorstore)

chatbot = ConversationalRetrievalChain(
    retriever=redis_product_retriever,
    combine_docs_chain=doc_chain,
    question_generator=question_generator
)