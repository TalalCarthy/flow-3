import streamlit as st
from config.chain_types import chain_types

from components.llm_config import llm_config
from components.memory_config import memory_config

from langchain.chains import RetrievalQA


def chain_config(session_prefix, start_key):
    chain_type = st.selectbox("Chain Type:", chain_types)

    configure = st.button('Configure Chain')

    if chain_type == 'LLM Chain':
        # configure template
        llm_config('llm_chain', start_key)
        memory_config('llm_chain', start_key + 10)
        if configure:
            pass
    elif chain_type == 'Retrieval QA':
        # configure llm
        # configure memory
        # configure template
        # configure retriever
        pass
    elif chain_type == 'Conversational Retrieval QA':
        # configure llm
        # configure memory
        # configure template
        # configure retriever
        pass
    elif chain_type == 'FLARE':
        # configure llm
        # configure memory
        # configure template
        # configure retriever
        pass


__all__ = ['chain_config']
