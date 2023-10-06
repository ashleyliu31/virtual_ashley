import os
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import tempfile

google_api_key='xxxxx'

def rag(question):
    # set up LLM and embedding 
    llm = GooglePalm(temperature=0, verbose=True,google_api_key=google_api_key)
    embedding = GooglePalmEmbeddings(google_api_key=google_api_key)
    # make temporary folder to for vector database
    tempfile.mkdtemp()
    persist_directory = tempfile.gettempdir()
    # load PDF files 
    filename = "info.pdf"
    pdf_path = os.path.join('assets', filename)
    loaders = [PyPDFLoader(pdf_path)]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    # set up text splitter 
    chunk_size =200
    chunk_overlap =10
    c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator = '.')
    splits = c_splitter.split_documents(docs)
    # put split docs into vector database
    vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory)
    # set up LLM prompt
    template = """
    Answer the question exactly according to the answers in the context. If the answer is not in the context, say I don't have that information. 
    Please answer in one complete sentence with subject and object. Please speak in the first person.  
    Context: {context}
    Question: {question}
    Helpful Answer:
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    # generate LLM response based on data retrieved from vector database
    result = qa_chain({"query": question})
    return result['result']