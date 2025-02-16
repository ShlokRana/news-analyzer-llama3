import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from ollama_llm import OllamaLLM

class NewsAnalyzer:
    def __init__(self):
        self.llm = OllamaLLM()
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def extract_article_content(self, url: str) -> str:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Get text content
            text = ' '.join([p.get_text() for p in soup.find_all('p')])
            return text.strip()
        except Exception as e:
            raise Exception(f"Error extracting content: {str(e)}")

    def create_vector_store(self, text: str):
        chunks = self.text_splitter.split_text(text)
        return FAISS.from_texts(chunks, self.embeddings)

    def get_summary(self, text: str) -> str:
        prompt = """
        Please provide a concise summary of the following news article:
        
        {text}
        
        Summary:
        """
        response = self.llm(prompt.format(text=text))
        return response

    def setup_qa_chain(self, vector_store):
        prompt_template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}

        Question: {question}
        Answer:"""
        
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            chain_type_kwargs={"prompt": PROMPT}
        )

    def answer_question(self, qa_chain, question: str) -> str:
        try:
            response = qa_chain({"query": question})
            return response['result']
        except Exception as e:
            return f"Error processing question: {str(e)}"