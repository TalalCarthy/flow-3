import streamlit as st
from modules.reset import reset

from components.chain_config import chain_config

# Reset the session
reset()

st.title("Configuration")

st.divider()
st.write("Planner:")

chain_config('planner', start_key=0)

st.divider()
st.write("Executor:")

chain_config('executor', start_key=2000)

st.divider()

if st.button("Set Configuration"):
    pass
