from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv('GEMINI_KEY')
os.environ["GROQ_API_KEY"] = os.getenv('grok')


def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

def load_in_vectord():
    loader = TextLoader(r"D:\GyanInc\FinanceBot\src\static\finance_adivce.txt")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # embeddings = OpenAIEmbeddings()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GEMINI_KEY )
    vectorstore = Chroma.from_documents(splits, embeddings, persist_directory="./chroma_db")


def str_to_json(text):
  start = text.find('{')
  end = text.rfind('}') + 1
  json_text = text[start:end]
  return json_text

def rag_model():
        # llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

        llm = ChatGroq(model="llama3-8b-8192")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GEMINI_KEY )
        
        vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings )
        # vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        retriever = vectorstore.as_retriever()
        prompt = PromptTemplate(
        input_variables=["context","question"],
        template='''Context: You are a financial advisor CHATBOT who studies the user information and advices them for better financial planning.
        User Information: {question}
        Note:
        Use provided user information for financial questions asked.
        Do not repeat the user information.
        Keep chat response precise, short, informative, and chatbot-friendly.
        '''
    )
        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return rag_chain