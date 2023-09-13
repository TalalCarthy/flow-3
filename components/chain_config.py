import streamlit as st

from config.chain_types import chain_types
from config.document_chain_types import document_chain_types

from components.llm_config import llm_config
from components.memory_config import memory_config
from components.template_config import template_config


def chain_config(session_prefix, start_key):
    chain_type = st.selectbox(
        "Chain Type:", chain_types,
        index=st.session_state.get(f'{session_prefix}_chain_type_index', 0), key=start_key)
    st.session_state[f'{session_prefix}_use_hyde'] = st.checkbox(
        "Use HyDE",
        value=st.session_state.get(f'{session_prefix}_use_hyde', False),
        key=start_key+1)

    st.session_state[f'{session_prefix}_chain_type_index'] = chain_types.index(
        chain_type)

    if chain_type == 'LLM Chain':
        with st.expander("LLM Chain Template"):
            template_config(f'{session_prefix}_llm_chain', start_key+2)
        with st.expander("LLM Chain LLM"):
            llm_config(f'{session_prefix}_llm_chain', start_key + 10)
        with st.expander("LLM Chain Memory"):
            memory_config(f'{session_prefix}_llm_chain', start_key + 50)
    elif chain_type == 'Retrieval QA':
        with st.expander("Retrieval QA Template"):
            template_config(f'{session_prefix}_retrieval_qa', start_key + 100)
        with st.expander("Retrieval QA LLM"):
            llm_config(f'{session_prefix}_retrieval_qa', start_key + 110)
        st.session_state[f'{session_prefix}_document_chain_type'] \
            = st.selectbox("Retrieval QA Document Chain Type:",
                           document_chain_types,
                           index=st.session_state.get(f'{session_prefix}_document_chain_type_index', 0))
        st.session_state[f'{session_prefix}_document_chain_type_index'] = document_chain_types.index(
            st.session_state[f'{session_prefix}_document_chain_type'])
    elif chain_type == 'Conversational Retrieval QA':
        with st.expander("Conversational Retrieval QA Template"):
            template_config(
                f'{session_prefix}_conversational_retrieval_qa', start_key + 200)
        with st.expander("Conversational Retrieval QA LLM"):
            llm_config(
                f'{session_prefix}_conversational_retrieval_qa', start_key + 210)
        with st.expander("Conversational Retrieval QA Memory"):
            memory_config(
                f'{session_prefix}_conversational_retrieval_qa', start_key + 220)
    elif chain_type == 'FLARE':
        with st.expander("FLARE Template"):
            template_config(f'{session_prefix}_flare', start_key + 300)
        with st.expander("FLARE LLM"):
            llm_config(f'{session_prefix}_flare', start_key + 310)
        with st.expander("FLARE Memory"):
            memory_config(f'{session_prefix}_flare', start_key + 320)
        st.session_state[f'{session_prefix}_flare_max_generation_len'] = st.number_input(
            "FLARE max generation length:", step=1, value=st.session_state.get(f'{session_prefix}_flare_max_generation_len', 164))
        st.session_state[f'{session_prefix}_flare_min_prob'] = st.slider(
            "FLARE minimum probability",
            value=st.session_state.get(
                f'{session_prefix}_flare_min_prob', 0.0),
            step=0.1,
            min_value=0.0,
            max_value=1.0)
    elif chain_type == 'QA over in-memory documents':
        with st.expander("QA over in-memory documents LLM"):
            llm_config(f'{session_prefix}_qa_chain', start_key + 400)
        st.session_state[f'{session_prefix}_document_chain_type'] = \
            st.selectbox(
            "QA Chain Document Chain Type:",
            document_chain_types,
            value=st.session_state[f'{session_prefix}_document_chain_type'])


__all__ = ['chain_config']
