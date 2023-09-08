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
    memory_type = st.selectbox("Select Memory Type:", memory_types)

    if memory_type == "None":
        st.session_state[f'temp_{session_prefix}_memory'] = None
    elif memory_type == "Conversational Buffer":
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True)

    elif memory_type == "Conversational Buffer Window":
        window_k = st.number_input("Window Limit:", step=1)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationBufferWindowMemory(
            k=window_k, memory_key="chat_history", return_messages=True)

    elif memory_type == "Entity":
        llm_config('entity_memory', start_key)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationEntityMemory(
            llm=st.session_state['entity_memory_llm'])

    elif memory_type == "Conversation Knowledge Graph":
        llm_config('conversation_knowledge_graph_memory', start_key + 10)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationKGMemory(
            llm=st.session_state['conversation_knowledge_graph_memory_llm'])

    elif memory_type == "Conversation Summary":
        llm_config('conversation_summary_memory', start_key + 20)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationSummaryMemory(
            llm=st.session_state['conversation_summary_memory_llm'])

    elif memory_type == "Conversation Summary Buffer":
        summary_buffer_token_limit = st.number_input("Token Limit:", step=1)
        llm_config('conversation_summary_buffer_memory', start_key + 30)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationSummaryBufferMemory(
            llm=st.session_state['conversation_summary_buffer_memory_llm'],
            max_token_limit=summary_buffer_token_limit)

    elif memory_type == "Conversation Token Buffer":
        conversation_token_buffer_token_limit = st.number_input(
            "Token Limit:", step=1)
        llm_config('conversation_token_buffer_memory', start_key + 40)
        st.session_state[f'temp_{session_prefix}_memory'] = ConversationTokenBufferMemory(
            llm=st.session_state['conversation_token_buffer_memory_llm'],
            max_token_limit=conversation_token_buffer_token_limit)


__all__ = ['memory_config']
