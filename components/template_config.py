import streamlit as st
from langchain.prompts import PromptTemplate


def template_config(session_prefix, start_key, default_value=None):
    if default_value:
        value = default_value
    else:
        value = '{prompt}'

    prompt_template_string = st.text_area(
        "Prompt Template:",
        st.session_state.get(f'{session_prefix}_template_string', value),
        520,
        key=start_key)

    st.session_state[f'{session_prefix}_template_string'] = prompt_template_string
    st.session_state[f'{session_prefix}_template'] = PromptTemplate(
        input_variables=["prompt"],
        template=prompt_template_string)


__all__ = ['template_config']
