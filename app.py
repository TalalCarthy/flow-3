import streamlit as st
from dotenv import load_dotenv
from modules.reset import reset


# Load environment variables
load_dotenv('.env')

# Reset the session
reset()

st.title("Flow 3: Talk over documents")
