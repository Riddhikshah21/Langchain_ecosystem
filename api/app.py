from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import ollama
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

# Load the LLM from Ollama
llm = ollama(model="phi3")  # Ensure Ollama is running locally and phi3 is downloaded

# Create prompts
prompt = ChatPromptTemplate.from_template("Write a poem on {topic} with 100 words")

# Bind prompts to the LLM
poem_chain = llm.bind(prompt)

# Add routes

add_routes(
    app,
    poem_chain,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)