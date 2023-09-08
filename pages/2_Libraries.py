import streamlit as st
from modules.reset import reset

# Reset the session
reset()

st.title("Libraries")

with st.form("Create a Library", clear_on_submit=True):
    name = st.text_input("Please write Library name")

    selected_data_sources = []
    for index, data_source in enumerate(st.session_state['data_sources']):
        add_source = st.checkbox(
            f"{data_source['name']} - {data_source['file_name']}")
        if add_source:
            selected_data_sources.append(index)

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

# Remove the libraries in bin (must be done before displaying the libraries)
for index in st.session_state['bin']:
    del st.session_state['libraries'][index]
st.session_state['bin'] = []


st.write("View Libraries")

for index, library in enumerate(st.session_state['libraries']):
    with st.expander(f"{library['name']}"):
        for i, source_index in enumerate(library['sources']):
            source = st.session_state['data_sources'][source_index]
            st.write(f"{i}. {source['name']} - {source['file_name']}")


st.divider()

st.write("Delete Libraries")

if st.button("Delete All Libraries"):
    st.session_state['libraries'] = []
    st.session_state['bin'] = []


for index, library in enumerate(st.session_state['libraries']):
    delete_key = st.button(
        f"🗑️ {library['name']}", key=index)
    if delete_key:
        st.session_state['bin'].append(index)
