import streamlit as st
from modules.reset import reset
from modules.file import get_document


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

with st.form("Create a DataSource", clear_on_submit=True):
    name = st.text_input('Please write DataSource name')

    uploaded_file = st.file_uploader(
        "Upload a file:", type=['txt', 'pdf', 'docx'])

    submitted = st.form_submit_button("Create DataSource")
    if submitted:
        if not name:
            st.error('Please give a name for the data source', icon="🔥")
        elif not uploaded_file:
            st.error('Please upload a file, Data Source cannot be empty', icon="🔥")
        else:
            document = get_document(uploaded_file)
            data_source = {'name': name, 'file': document,
                           'file_name': uploaded_file.name}
            st.session_state['data_sources'].append(data_source)
            st.success('Data Sources created successfully', icon="✅")
            # del uploaded_file  # KILL IT !!!

st.divider()

st.write('View DataSources')
source_names = (source['name'] for source in st.session_state['data_sources'])

for index, source in enumerate(st.session_state['data_sources']):
    with st.expander(f'{index}. {source["name"]}'):
        st.write(source['file_name'])


st.button("Clear Data Sources", on_click=reset_sources_array)

bin = st.multiselect("Delete:", source_names)
st.button("Clear bin", on_click=remove_sources, args=[bin])
