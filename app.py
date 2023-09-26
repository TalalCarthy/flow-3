import os
import streamlit as st
from dotenv import load_dotenv
from modules.reset import reset


# config API stuff
try:
    load_dotenv('.env')
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("API key not found in environment variable or .env file.")
except FileNotFoundError:
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("API key not found in environment variable or .env file.")

# Reset the session
reset()

st.title("Flow 3: Talk over documents")
st.write("Carthy.ai production")
