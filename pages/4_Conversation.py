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
    use_planner = st.checkbox(
        "Use Planner", value=st.session_state['use_planner'])
    if use_planner:
        with st.expander("Planner"):
            chain_sidebar_config('planner', 3000)
        with st.expander("Executor"):
            chain_sidebar_config('executor', 4000)
    else:
        chain_sidebar_config('executor', 4000)

    st.session_state['use_planner'] = use_planner

    st.divider()

    # choose execution mode (regular mode, no context planner, context planner)

# Chat

if prompt := st.chat_input("Enter a prompt"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())

        response = st.session_state['executor_chain'].run(
            prompt, callbacks=[st_callback])

        # plan_response_string = planner_chain.run(prompt=prompt)
        # plan_response = json.loads(plan_response_string)

        # if st.session_state['use_planner']:
        #     for step in plan_response:
        #         res = st.session_state['chain'].run(step)
        #         with st.expander(step):
        #             st.write(res)
        #     response = res
        # else:
        #     response = st.session_state['chain'].run(
        #         prompt, callbacks=[st_callback]
        #     )

        st.write(response)
        # st.json(plan_response)
