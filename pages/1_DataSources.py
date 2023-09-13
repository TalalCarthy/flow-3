import streamlit as st
from modules.reset import reset
from modules.file import get_document

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

# Remove the data sources
for index in st.session_state['bin']:
    del st.session_state['data_sources'][index]
st.session_state['bin'] = []


if st.button("Clear Data Sources"):
    st.session_state['data_sources'] = []
    st.session_state['bin'] = []

key = 0
for data_source in st.session_state['data_sources']:
    delete_key = st.button(
        f"🗑️ {data_source['name']} - {data_source['file_name']}", key=key)
    if delete_key:
        st.session_state['bin'].append(key)
    key += 1
