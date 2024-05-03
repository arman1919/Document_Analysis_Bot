from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

openai_api_key = "openai_api_key"




class Doc_Reader:
    
    
    def __init__(self,doc_path):
        
        
        self.vectorDB = self.create_db(self.read_pdf(doc_path),openai_api_key)
        
        self.llm = ChatOpenAI(openai_api_key= openai_api_key,model_name='gpt-3.5-turbo')
    
        self.llm.temperature = 0.1
        
        
        self.prompt = """system: You are the representative of this document.
             write only about what is written in the document, do not invent it.
             if you don't know the answer, say you don't know.
             the answer is in the language in which the question is being asked,
             """
             
             
     
        
    def get_answer(self,query):
        
        qa_chain = RetrievalQA.from_chain_type(
        llm=self.llm,
        chain_type='stuff',
        retriever=self.vectorDB.as_retriever()
        )
        answer = qa_chain.invoke(self.prompt+query)
        
        return answer['result']
       
        
        
        
    @staticmethod
    def read_pdf(path):
    
        loader = PyPDFLoader(path)
        pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        return text_splitter.split_documents(pages)

    @staticmethod
    def create_db(docs,openai_api_key):
    
        embedding = OpenAIEmbeddings(openai_api_key = openai_api_key,model_name = "text-embedding-3-small")
        
        return FAISS.from_documents(docs, embedding)
    
