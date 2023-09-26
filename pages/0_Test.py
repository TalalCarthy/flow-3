import os
import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from modules.file import get_document
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

import sys
__import__('pysqlite3')


os.system("playwright install")


sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


st.title("Scrape test")


prompt = st.text_input("Prompt:")
url = st.text_input("URL:")


if st.button("Submit"):
    loader = AsyncChromiumLoader([url])
    html = loader.load()

    llm = ChatOpenAI(model='gpt-4', temperature=0.0)

    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    embedding_function = OpenAIEmbeddings()

    split_docs = text_splitter.split_documents(html)
    db = Chroma.from_documents(split_docs, embedding_function)
    retriever = db.as_retriever()

    test_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever
    )

    response = test_chain.run(prompt)
    st.write(response)
