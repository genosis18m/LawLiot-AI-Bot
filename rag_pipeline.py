from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate



#Setup LLM (Use DeepSeek R1 with Groq)
# In rag_pipeline.py
llm_model = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key="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"  # Add this line
)

#Retrieve Docs

def retrieve_docs(query):
    return faiss_db.similarity_search(query)


def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

#Step3: Answer Question

custom_prompt_template = """
Kindly use those pieces of information that are provided in the context to answer user's question.
If you dont know the answer, just say you dont have that answer, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""
def answer_query(documents, model, query):  # Ensure this is defined
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})

