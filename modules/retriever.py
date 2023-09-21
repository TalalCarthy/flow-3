import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


def get_retriever():
    text_splitter = CharacterTextSplitter(
        chunk_size=st.session_state['splitter_chunk_size'],
        chunk_overlap=st.session_state['splitter_chunk_overlap'])

    docs = []
    st.json(st.session_state['library'])
    st.json(st.session_state['data_sources'])
    for source in st.session_state['library']['sources']:
        docs.extend(st.session_state['data_sources'][source]['file'])

    docs = text_splitter.split_documents(docs)
    db = Chroma.from_documents(docs, OpenAIEmbeddings())
    return db.as_retriever()


__all__ = ['get_retriever']
