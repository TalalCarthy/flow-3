from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.schema.document import Document
from langchain.document_loaders import JSONLoader
from langchain.document_loaders.csv_loader import CSVLoader


def save_binary(uploaded_file, save_path):
    with open(save_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())


def get_document(uploaded_file):
    if uploaded_file.name.endswith('.txt'):
        text = uploaded_file.getvalue()
        metadata = {"source": uploaded_file.name}
        return [Document(page_content=text, metadata=metadata)]
    elif uploaded_file.name.endswith('.pdf'):
        save_binary(uploaded_file, './files/pdf.pdf')
        return PyPDFLoader('./files/pdf.pdf').load()
    elif uploaded_file.name.endswith('.docx'):
        save_binary(uploaded_file, './files/docx.docx')
        return Docx2txtLoader('./files/docx.docx').load()
    elif uploaded_file.name.endswith('.json'):
        with open('./files/json.json', 'w') as f:
            f.write(uploaded_file.getvalue())
        return JSONLoader('./files/json.json',
                          jq_schema='',
                          text_content=False)
    elif uploaded_file.name.endswith('.csv'):
        save_binary(uploaded_file, './files/csv.csv')
        return CSVLoader('./files/csv.csv')

    return None


__all__ = ['get_document']
