import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
# from langchain.chains import DocumentQA
from langchain.chains import ConversationalRetrievalChain


def get_chain(chain_type, document_chain_type, retriever):
    if chain_type == 'Retrieval QA':
        st.session_state['chain'] = RetrievalQA.from_chain_type(
            llm=st.session_state['chat_llm'],
            chain_type=document_chain_type,
            retriever=retriever
        )
    elif chain_type == 'Document QA':
        # st.session_state['chain'] = DocumentQA.from_chain_type(
        #     llm=st.session_state['chat_llm'],
        #     retriever=retriever
        # )
        pass
    elif chain_type == 'Conversational Retrieval QA':
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True)
        st.session_state['chain'] = ConversationalRetrievalChain.from_llm(
            st.session_state['chat_llm'],
            retriever,
            memory=memory
        )


__all__ = ['get_chain']
