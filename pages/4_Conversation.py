import streamlit as st
from modules.reset import reset
from modules.retriever import get_retriever
from modules.chain import get_chain
from modules.planner import planner_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler
import json

# Reset the session
reset()

with st.sidebar:
    # Token Limit

    # select library
    library_names = [library['name']
                     for library in st.session_state['libraries']]
    selected_library_name = st.selectbox("Select a Library", library_names)
    selected_library = next(
        (library for library in st.session_state['libraries'] if library['name'] == selected_library_name), None)

    st.divider()

    splitter_chunk_size = st.number_input(
        "Text Splitter Chunk Size", min_value=0,
        value=st.session_state['splitter_chunk_size'])
    splitter_chunk_overlap = st.number_input(
        "Text Splitter Chunk Overlap", min_value=0,
        value=st.session_state['splitter_chunk_overlap'])

    st.divider()

    document_chain_type = st.selectbox('Select Document Chain Type', [
        'stuff', 'refine', 'map_reduce', 'map_rerank'])
    chain_type = st.selectbox('Select Chain Type', [
                              'Retrieval QA', 'Document QA',
                              'Conversational Retrieval QA'])

    st.divider()

    model_name = st.text_input("Model Name", value="gpt-4")
    model_temperature = st.slider(
        "Model Temperature", min_value=0.0, max_value=2.0, value=0.2, step=0.1)

    use_planner = st.checkbox("Use Planner")

    if st.button("Set Configuration"):
        if selected_library:
            st.session_state['library'] = selected_library
        st.session_state['splitter_chunk_overlap'] = splitter_chunk_overlap
        st.session_state['splitter_chunk_size'] = splitter_chunk_size

        retriever = get_retriever()

        st.session_state['chat_llm'] = ChatOpenAI(
            model=model_name, temperature=model_temperature)

        get_chain(chain_type=chain_type,
                  document_chain_type=document_chain_type,
                  retriever=retriever)
        st.session_state['use_planner'] = use_planner

    # choose execution mode (regular mode, no context planner, context planner)

# Chat

if prompt := st.chat_input("Enter a prompt"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())

        plan_response_string = planner_chain.run(prompt=prompt)
        plan_response = json.loads(plan_response_string)

        if st.session_state['use_planner']:
            for step in plan_response:
                res = st.session_state['chain'].run(step)
                with st.expander(step):
                    st.write(res)
            response = res
        else:
            response = st.session_state['chain'].run(
                prompt, callbacks=[st_callback]
            )

        st.write(response)
        st.json(plan_response)

# $env:LANGCHAIN_TRACING_V2=true
# $env:LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# $env:LANGCHAIN_API_KEY="ls__894e183705db4121be3ebbdeaee8b1ed"
# $env:LANGCHAIN_PROJECT="flow"
