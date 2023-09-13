import streamlit as st


def reset():
    if 'data_sources' not in st.session_state:
        st.session_state['data_sources'] = []
    if 'libraries' not in st.session_state:
        st.session_state['libraries'] = []
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
    if 'reconfigure_chain' not in st.session_state:
        st.session_state['reconfigure_chain'] = True


__all__ = ['reset']
