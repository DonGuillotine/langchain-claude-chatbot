from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatAnthropic(streaming=True, verbose=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

messages = [
    HumanMessage(content="Translate this sentence from English to Spanish. I love programming.")
]
chat(messages)

