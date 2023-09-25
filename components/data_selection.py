import streamlit as st
from config.data_source_types import data_source_types
from modules.file import get_document

from langchain.document_loaders import AirtableLoader
from langchain.document_loaders import BSHTMLLoader


def submit_handler(name, file_name, document):
    data_source = {'name': name, 'file': document,
                   'file_name': file_name}
    st.session_state['data_sources'].append(data_source)
    st.success('Data Sources created successfully', icon="✅")
    # del uploaded_file  # KILL IT !!!


def data_selection():
    selected_type = st.selectbox(
        'Data Source type', data_source_types, placeholder="Choose your option...")
    with st.form("Create a DataSource", clear_on_submit=True):
        name = st.text_input('Please write DataSource name')
        if selected_type == 'upload file':
            uploaded_file = st.file_uploader(
                "Upload a file:", type=['txt', 'pdf', 'docx', 'json', 'csv'])
            submitted = st.form_submit_button("Create DataSource")
            if submitted:
                if not name:
                    st.error('Please give a name for the data source', icon="🔥")
                elif not uploaded_file:
                    st.error(
                        'Please upload a file, Data Source cannot be empty', icon="🔥")
                else:
                    submit_handler(name, uploaded_file.name,
                                   get_document(uploaded_file))
        elif selected_type == 'AirTable':
            airtable_api_key = st.text_input(
                'AirTable API key',
                value=st.session_state.get('AIRTABLE_API_KEY', ''))
            airtable_base_id = st.text_input('AirTable Base ID')
            airtable_table_id = st.text_input('AirTable Table ID')

            st.session_state['AIRTABLE_API_KEY'] = airtable_api_key
            if st.form_submit_button("Create DataSource"):
                submit_handler(name, name, AirtableLoader(
                    airtable_api_key,
                    airtable_table_id,
                    airtable_base_id).load())

        elif selected_type == 'HTML page':
            html_link = st.text_input('Path/Link to HTML page')
            if st.form_submit_button("Create DataSource"):
                submit_handler(name, name, BSHTMLLoader(html_link).load())


__all__ = ['data_selection']
