import streamlit as st

from modules.retriever import get_retriever

from langchain.chains import LLMChain
from langchain.chains import RetrievalQA


def set_chain(session_prefix, chain_type):
    if chain_type == 'LLM Chain':
        st.session_state[f'{session_prefix}_chain'] = LLMChain(
            llm=st.session_state[f'{session_prefix}_llm_chain_llm'],
            prompt=st.session_state[f'{session_prefix}_llm_chain_template'],
            memory=st.session_state[f'{session_prefix}_llm_chain_memory'])
    elif chain_type == 'Retrieval QA':
        st.session_state[f'{session_prefix}_chain'] = RetrievalQA.from_chain_type(
            llm=st.session_state[f'{session_prefix}_retrieval_qa'],
            chain_type=st.session_state[f'{session_prefix}_document_chain_type'],
            retriever=get_retriever()
        )
    elif chain_type == 'Conversational Retrieval QA':
        pass
    elif chain_type == 'FLARE':
        pass
    elif chain_type == 'QA over in-memory documents':
        pass


__all__ = ['set_chain']
