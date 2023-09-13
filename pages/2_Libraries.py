import streamlit as st
from modules.reset import reset


def remove_libraries(bin):
    for index, library in enumerate(st.session_state['libraries']):
        if library['name'] in bin:
            del st.session_state['libraries'][index]


def reset_library_array():
    st.session_state['libraries'] = []


# Reset the session
reset()

st.title("Libraries")

with st.form("Create a Library", clear_on_submit=True):
    name = st.text_input("Please write Library name")

    source_names = (source['name']
                    for source in st.session_state['data_sources'])
    selected_data_source_names = st.multiselect(
        "Select Data Sources:", source_names)

    selected_data_sources = [index for index, source in enumerate(
        st.session_state['data_sources']) if source['name'] in selected_data_source_names]

    submitted = st.form_submit_button("Create Library")
    if submitted:
        if not name:
            st.error("Please give a name for the library")
        elif selected_data_sources == []:
            st.error("Library cannot be empty, add some data sources")
        else:
            library = {'name': name, 'sources': selected_data_sources}
            st.session_state['libraries'].append(library)
            st.success("Library created successfully", icon="✅")

st.divider()
st.write("View Libraries")

for index, library in enumerate(st.session_state['libraries']):
    with st.expander(f"{library['name']}"):
        for i, source_index in enumerate(library['sources']):
            source = st.session_state['data_sources'][source_index]
            st.write(f"{i}. {source['name']} - {source['file_name']}")


st.divider()
st.write("Delete Libraries")
st.button("Delete All Libraries", on_click=reset_library_array)

library_names = (library['name'] for library in st.session_state['libraries'])
bin = st.multiselect("Delete:", library_names)
st.button("Clear bin", on_click=remove_libraries, args=[bin])
