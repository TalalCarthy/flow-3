import streamlit as st
from modules.reset import reset

from components.chain_config import chain_config

# Reset the session
reset()

st.title("Configuration")

st.write("Text Splitter:")
st.session_state['splitter_chunk_size'] = st.number_input(
    "Text Splitter Chunk Size", min_value=0,
    value=st.session_state['splitter_chunk_size'])
st.session_state['splitter_chunk_overlap'] = st.number_input(
    "Text Splitter Chunk Overlap", min_value=0,
    value=st.session_state['splitter_chunk_overlap'])

st.divider()
st.write("Planner:")

chain_config('planner', start_key=0)

st.divider()
st.write("Executor:")

chain_config('executor', start_key=2000)

st.divider()
