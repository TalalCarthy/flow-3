import streamlit as st
from modules.reset import reset

from components.data_selection import data_selection


def remove_sources(bin):
    for index, source in enumerate(st.session_state['data_sources']):
        if source['name'] in bin:
            del st.session_state['data_sources'][index]


def reset_sources_array():
    st.session_state['data_sources'] = []


# Reset the session
reset()

st.title("Data Sources")

st.write("DataSource management")


data_selection()

st.divider()

st.write('View DataSources')
source_names = (source['name'] for source in st.session_state['data_sources'])

for index, source in enumerate(st.session_state['data_sources']):
    with st.expander(f'{index}. {source["name"]}'):
        st.write(source['file_name'])


st.button("Clear Data Sources", on_click=reset_sources_array)

bin = st.multiselect("Delete:", source_names)
st.button("Clear bin", on_click=remove_sources, args=[bin])
