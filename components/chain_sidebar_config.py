import streamlit as st

from modules.retriever import get_retriever
from modules.chain import set_chain

from config.chain_types import chain_types


def chain_change_handler():
    st.session_state['reconfigure_chain'] = True


def chain_sidebar_config(session_prefix, start_key):
    library_names = [library['name']
                     for library in st.session_state['libraries']]
    selected_library_index = st.session_state.get(
        'selected_library_index', 0)
    selected_library_name = st.selectbox(
        "Select Library:",
        library_names,
        index=selected_library_index,
        key=start_key,
        on_change=chain_change_handler)

    st.divider()

    selected_chain_type_index = st.session_state.get(
        'selected_chain_type_index', 0)
    chain_type = st.selectbox(
        'Select Chain Type',
        chain_types,
        index=selected_chain_type_index,
        key=start_key+2,
        on_change=chain_change_handler)

    st.divider()

    if st.session_state['reconfigure_chain']:
        if selected_library_name:
            selected_library = next(
                (library for library in st.session_state['libraries']
                 if library["name"] == selected_library_name),
                None)
            st.session_state['library'] = selected_library
        st.session_state['selected_chain_type_index'] = chain_types.index(
            chain_type)
        st.session_state['selected_library_index'] = library_names.index(
            selected_library_name)

        set_chain(session_prefix, chain_type)
    st.session_state['reconfigure_chain'] = False


__all__ = ['chain_sidebar_config']
