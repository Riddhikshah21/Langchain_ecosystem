import requests
import streamlit as st

def get_llm_response(input_text):
    response = requests.post("https://localhost:8000/poem/invoke",
                             json = {'input':{'topic':input_text}})
    return response.json()['output']['content']

st.title("Langchain demo with Phi3 api")
input_text = st.text_input("Write a poem on")
if input_text:
    st.write(get_llm_response(input_text=input_text))