import streamlit as st
from config.templates import planner_template


def reset():
    if 'data_sources' not in st.session_state:
        st.session_state['data_sources'] = []
    if 'libraries' not in st.session_state:
        st.session_state['libraries'] = []
    if 'key' not in st.session_state:
        st.session_state['key'] = 0
    if 'bin' not in st.session_state:
        st.session_state['bin'] = []
    if 'library' not in st.session_state:
        st.session_state['library'] = {}
    if 'splitter_chunk_size' not in st.session_state:
        st.session_state['splitter_chunk_size'] = 2000
    if 'splitter_chunk_overlap' not in st.session_state:
        st.session_state['splitter_chunk_overlap'] = 0
    if 'use_planner' not in st.session_state:
        st.session_state['use_planner'] = False
    if 'planner_template' not in st.session_state:
        st.session_state['planner_template'] = planner_template


__all__ = ['reset']
