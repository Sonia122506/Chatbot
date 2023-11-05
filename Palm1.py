#pip install openai
import streamlit as st
import google.generativeai as palm

palm.api_key=palm.configure(api_key="AIzaSyB1JunjrZuRTcWxZFocRTJ8u78YOSkbNfw")# Replace with your actual API key

models=[model for model in palm.list_models()]
for model in models:
    print(model.name)
st.title("Medical Chatbot")
def ask_medical_question(user_input):
    prompt = "You are a medical chatbot. Answer the following medical user_input:\n\n" + user_input + "\nAnswer:"
    response = palm.generate_text(model="models/text-bison-001",prompt=prompt,temperature=0.99,max_output_tokens=800,)
    return response        

if "inputs" not in st.session_state:
    st.session_state.inputs=[]
for i in st.session_state.inputs:
    with st.chat_message(i["role"]):
        st.markdown(i["content"])

user_input=st.chat_input("Ask Anything 🤷‍♂️")

if user_input:
    user_message=st.chat_message("user")
    user_message.markdown(user_input)
    st.session_state.inputs.append({"role":"user","content":user_input})

    ai_message=st.chat_message("assistant")
    with ai_message:
      resource=ask_medical_question(user_input)
      st.markdown(resource)
      


