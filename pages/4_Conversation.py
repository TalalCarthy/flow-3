import streamlit as st
import json


from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler

from modules.reset import reset
from modules.retriever import get_retriever
from modules.chain import set_chain

from config.chain_types import chain_types

from components.chain_sidebar_config import chain_sidebar_config

# Reset the session
reset()

with st.sidebar:
    use_enhancer = st.checkbox(
        "Use Prompt Enhancer",
        value=st.session_state.get("use_enhancer", False)
    )
    use_planner = st.checkbox(
        "Use Planner", value=st.session_state['use_planner'])
    if use_planner:
        with st.expander("Planner"):
            chain_sidebar_config('planner', 10000)
        with st.expander("Executor"):
            chain_sidebar_config('executor', 12000)
    else:
        chain_sidebar_config('executor', 10000)

    st.session_state['use_planner'] = use_planner
    st.session_state['use_enhancer'] = use_enhancer

    st.divider()

    # choose execution mode (regular mode, no context planner, context planner)

# Chat

if prompt := st.chat_input("Enter a prompt"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        query = prompt
        if st.session_state['use_enhancer']:
            query = st.session_state['prompt_enhancer_chain'](prompt)['text']
            with st.expander("Enhanced Prompt"):
                st.write(query)

        if st.session_state['use_planner']:
            plan_response_string = st.session_state['planner_chain'].run(
                query)
            plan_response = json.loads(plan_response_string)
            for step in plan_response:
                res = st.session_state['executor_chain'].run(step)
                with st.expander(step):
                    st.write(res)
            response = res
        else:
            response = st.session_state['executor_chain'].run(
                query, callbacks=[st_callback])

        st.write(response)
