import streamlit as st
from modules.reset import reset

from components.chain_config import chain_config

# Reset the session
reset()


st.title("Configuration")

st.divider()
st.write("Planner:")

planner_template_string = st.text_area(
    "Planner Prompt Template:", st.session_state['planner_template'], 520)

chain_config('planner')

st.divider()
st.write("Executor:")

chain_config('executor', start_key=10)

st.divider()

if st.button("Set Configuration"):
    st.session_state["planner_template"] = planner_template_string
