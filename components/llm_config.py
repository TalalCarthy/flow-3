import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


def llm_config(session_prefix, start_key):
    llm_model_is_chat = st.checkbox(
        "Chat Model", st.session_state.get(
            f"{session_prefix}_model_is_chat", ''),
        key=start_key)
    temperature = st.slider("Model Temperature:",
                            value=st.session_state.get(
                                f"{session_prefix}_temperature", 0.0),
                            min_value=0.0, max_value=2.0, step=0.1,
                            key=start_key+1)
    model_name = st.text_input(
        "Model Name:", value=st.session_state.get(f"{session_prefix}_model_name", ''),
        key=start_key+2)

    st.session_state[f"{session_prefix}_model_is_chat"] = llm_model_is_chat
    st.session_state[f"{session_prefix}_temperature"] = temperature
    st.session_state[f"{session_prefix}_model_name"] = model_name

    if llm_model_is_chat:
        llm = ChatOpenAI(model_name, temperature=temperature)
    else:
        llm = OpenAI(model_name, temperature=temperature)
    st.session_state[f"temp_{session_prefix}_llm"] = llm


__all_ = ['choose_llm']
