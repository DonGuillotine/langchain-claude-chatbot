"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message

from conversation_chain import chatbot


# From here down is all the StreamLit UI.
st.set_page_config(page_title="Digital Support Gurus", page_icon=":robot:")
st.header("Smart Customer Support Chatbot")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


chat_history = []



question = "Hi! What are you looking for today?"
    
    

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


user_input = get_text()


if user_input:
    result = chatbot(
        {"question": question, "chat_history": chat_history}
    )
    chat_history.append((result["question"], result["answer"]))
    question = result["question"]

    st.session_state.past.append(result["question"])
    st.session_state.generated.append(result["answer"])

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")