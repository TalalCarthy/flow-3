import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


def llm_config(session_prefix, start_key):
    llm_model_is_chat = st.checkbox(
        "Chat Model", value=st.session_state.get(
            f"{session_prefix}_llm_model_is_chat", True),
        key=start_key)
    temperature = st.slider("Model Temperature:",
                            value=st.session_state.get(
                                f"{session_prefix}_llm_temperature", 0.0),
                            min_value=0.0, max_value=2.0, step=0.1,
                            key=start_key+1)
    model_name = st.text_input(
        "Model Name:", value=st.session_state.get(f"{session_prefix}_llm_model_name", 'gpt-4'),
        key=start_key+2)

    st.session_state[f"{session_prefix}_llm_model_is_chat"] = llm_model_is_chat
    st.session_state[f"{session_prefix}_llm_temperature"] = temperature
    st.session_state[f"{session_prefix}_llm_model_name"] = model_name

    if llm_model_is_chat:
        llm = ChatOpenAI(model=model_name if model_name else 'gpt-4',
                         temperature=temperature if temperature else 0.0)
    else:
        llm = OpenAI(model=model_name if model_name else '',
                     temperature=temperature if temperature else 0.0)
    st.session_state[f"{session_prefix}_llm"] = llm


__all_ = ['llm_config']
