import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI


def get_planner():
    planner_prompt = PromptTemplate(
        input_variables=['prompt'],
        template=st.session_state['planner_template'])
    llm = OpenAI(temperature=0)
    planner_chain = LLMChain(llm=llm, prompt=planner_prompt)


__all__ = ['planner_chain']
