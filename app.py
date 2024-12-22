from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please repond to the user queries and if you do not know the answer reply 'I do not know the answer'"),
        ("user","Question: {question}")
    ]
)

#streamlit framework
st.title("Riddhi's personal Chatbot")
input_text = st.text_input("Please enter your query here!")

#ollama LLM: Phi3 model 
llm = Ollama(model="phi3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))