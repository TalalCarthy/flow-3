import streamlit as st
from config.memory_types import memory_types
from components.llm_config import llm_config

from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationEntityMemory
from langchain.memory import ConversationKGMemory
from langchain.memory import ConversationSummaryMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.memory import ConversationTokenBufferMemory


def memory_config(session_prefix, start_key):
    memory_type = st.selectbox("Select Memory Type:",
                               memory_types,
                               index=st.session_state.get(f'{session_prefix}_memory_type', 0), key=start_key)
    st.session_state[f'{session_prefix}_memory_type'] = memory_types.index(
        memory_type)

    if memory_type == "None":
        st.session_state[f'{session_prefix}_memory'] = None
    elif memory_type == "Conversational Buffer":
        st.session_state[f'{session_prefix}_memory'] = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True)

    elif memory_type == "Conversational Buffer Window":
        window_k = st.number_input(
            "Window Limit:",
            step=1,
            value=st.session_state.get(f'{session_prefix}_window_k', 0),
            key=start_key+1)
        st.session_state[f'{session_prefix}_window_k'] = window_k
        st.session_state[f'{session_prefix}_memory'] = ConversationBufferWindowMemory(
            k=window_k, memory_key="chat_history", return_messages=True)

    elif memory_type == "Entity":
        llm_config(f'{session_prefix}_entity_memory', start_key+10)
        st.session_state[f'{session_prefix}_memory'] = ConversationEntityMemory(
            llm=st.session_state.get(f'{session_prefix}_entity_memory_llm', None))

    elif memory_type == "Conversation Knowledge Graph":
        llm_config(
            f'{session_prefix}_conversation_knowledge_graph_memory', start_key+20)
        st.session_state[f'{session_prefix}_memory'] = ConversationKGMemory(
            llm=st.session_state.get(f'{session_prefix}_conversation_knowledge_graph_memory_llm', None))

    elif memory_type == "Conversation Summary":
        llm_config(
            f'{session_prefix}_conversation_summary_memory', start_key+30)
        st.session_state[f'{session_prefix}_memory'] = ConversationSummaryMemory(
            llm=st.session_state.get(f'{session_prefix}_conversation_summary_memory_llm', None))

    elif memory_type == "Conversation Summary Buffer":
        summary_buffer_token_limit = st.number_input(
            "Token Limit:",
            step=1,
            value=st.session_state.get(f'{session_prefix}_buffer_token_limit', 0))
        st.session_state[f'{session_prefix}_buffer_token_limit'] = summary_buffer_token_limit
        llm_config(
            f'{session_prefix}_conversation_summary_buffer_memory', start_key+40)
        st.session_state[f'{session_prefix}_memory'] = ConversationSummaryBufferMemory(
            llm=st.session_state.get(
                f'{session_prefix}_conversation_summary_buffer_memory_llm', None),
            max_token_limit=summary_buffer_token_limit)

    elif memory_type == "Conversation Token Buffer":
        conversation_token_buffer_token_limit = st.number_input(
            "Token Limit:",
            step=1,
            value=st.session_state.get(
                f'{session_prefix}_buffer_token_limit', 0),
            key=start_key+41)
        st.session_state[f'{session_prefix}_buffer_token_limit'] = conversation_token_buffer_token_limit
        llm_config(
            f'{session_prefix}_conversation_token_buffer_memory', start_key + 50)
        st.session_state[f'{session_prefix}_memory'] = ConversationTokenBufferMemory(
            llm=st.session_state.get(
                f'{session_prefix}_conversation_token_buffer_memory_llm', None),
            max_token_limit=conversation_token_buffer_token_limit)


__all__ = ['memory_config']
