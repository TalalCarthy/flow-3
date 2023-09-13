import streamlit as st

from modules.retriever import get_retriever

from langchain.chains import LLMChain
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import FlareChain


def set_chain(session_prefix, chain_type):
    if chain_type == 'LLM Chain':
        st.session_state[f'{session_prefix}_chain'] = LLMChain(
            llm=st.session_state[f'{session_prefix}_llm_chain_llm'],
            prompt=st.session_state[f'{session_prefix}_llm_chain_template'],
            memory=st.session_state[f'{session_prefix}_llm_chain_memory'],
            verbose=True)
    elif chain_type == 'Retrieval QA':
        st.session_state[f'{session_prefix}_chain'] = RetrievalQA.from_chain_type(
            llm=st.session_state[f'{session_prefix}_retrieval_qa_llm'],
            chain_type=st.session_state[f'{session_prefix}_document_chain_type'],
            retriever=get_retriever()
        )
    elif chain_type == 'Conversational Retrieval QA':
        st.session_state[f'{session_prefix}_chain'] = \
            ConversationalRetrievalChain.from_llm(
            st.session_state[f'{session_prefix}_conversational_retrieval_qa_llm'],
            get_retriever(),
            memory=st.session_state[f'{session_prefix}_conversational_retrieval_qa_memory']
        )
    elif chain_type == 'FLARE':
        st.session_state[f'{session_prefix}_chain'] = FlareChain.from_llm(
            st.session_state[f'{session_prefix}_flare_llm'],
            retriever=get_retriever(),
            max_generation_len=st.session_state[f'{session_prefix}_flare_max_generation_len'],
            min_prob=st.session_state[f'{session_prefix}_flare_min_prob']
        )
    elif chain_type == 'QA over in-memory documents':
        pass


__all__ = ['set_chain']
