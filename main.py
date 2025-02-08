from langchain_groq import ChatGroq
from database import faiss_db
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


llm_model = ChatGroq(model = "deepseek-r1-distill-llama-70b" , api_key = api_key)

def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

custom_prompt_template = """
Use the piece of information provided in the context to answer user's question.
If you dont know the answer, justify that you dont know, dont try to make up an answer
Dont provide anyting out of the given context
Question: {question}
Context: {context}
Answer:
"""

def answer_quer(documents , model , query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question":query , "context":context})

