import streamlit as st
from modules.reset import reset

from components.chain_config import chain_config
from components.llm_config import llm_config
from components.template_config import template_config

from config.templates import enhancer_template

from langchain.chains import LLMChain


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
st.write("Prompt Enhancer")

llm_config('prompt_enhancer', start_key=2700)
template_config('prompt_enhancer', start_key=2800,
                default_value=enhancer_template)
st.session_state['prompt_enhancer_chain'] = LLMChain(
    llm=st.session_state.get('prompt_enhancer_llm', None),
    prompt=st.session_state.get('prompt_enhancer_template', None))
