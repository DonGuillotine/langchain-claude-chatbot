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


summary = """
You can ask our Chatbot about:

- Earrings: Styles, materials, care instructions.
- Pillow: Types, sizes, recommendations.
- Phone case: Compatibility, designs, protection.
- Chair: Types (e.g., office, gaming), features, comfort.
- Shoes: Styles, sizes, brands, materials.
- Baby product: Safety, recommendations, usage instructions.
- Office products: Stationery, organization, productivity tools.
- Backpack: Sizes, features, durability, brands.
- Furniture: Types (e.g., sofas, tables), materials, assembly.
- Grocery: Products availability, prices, dietary preferences.
- Light bulb: Types (e.g., LED, incandescent), wattage, compatibility.
"""

st.markdown(summary)

    

def get_text(user_input):
    input_text = st.text_input("You: ", user_input, key="input")
    return input_text


chat_history = []


question = "Hello, I need your assitance"

user_input = get_text(question)

if user_input:
    question = user_input
    result = chatbot(
        {"question": user_input, "chat_history": chat_history}
    )
    chat_history.append((result["question"], result["answer"]))

    st.session_state.past.append(result["question"])
    st.session_state.generated.append(result["answer"])

    question = result["question"]

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")