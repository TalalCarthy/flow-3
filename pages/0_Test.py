from modules.file import get_document
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import streamlit as st
import sys
__import__('pysqlite3')


sys.modules['sqlite3'] = sys.modules.pip('pysqlite3')


st.title("Chroma test")

st.write(sys.version)
st.write(sys.version_info)

prompt = st.text_input("Prompt")
uploaded_file = st.file_uploader("Upload file")


if st.button("Submit"):
    docs = get_document(uploaded_file)
    llm = ChatOpenAI(model='gpt-4', temperature=0.0)

    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    embedding_function = OpenAIEmbeddings()

    split_docs = text_splitter.split_documents(docs)
    db = Chroma.from_documents(split_docs, embedding_function)
    retriever = db.as_retriever()

    test_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever
    )

    response = test_chain.run(prompt)
    st.write(response)
