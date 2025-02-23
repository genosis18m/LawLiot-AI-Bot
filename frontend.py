from rag_pipeline import retrieve_docs, answer_query, llm_model

#Step1: Setup Upload PDF functionality
import streamlit as st

uploaded_file = st.file_uploader("Upload PDF",
                                    type="pdf",
                                    accept_multiple_files=False
                                )


#Step2: Chatbot Skeleton (Question & Answer)

user_query = st.text_area("Enter your prompt: ", height=150 , placeholder= "Law Keeper in Your Service")

ask_question = st.button("ASK LAWLIOT")

if ask_question:

    if uploaded_file: 

        st.chat_message("user").write(user_query)

        # RAG Pipeline
        retrieved_docs=retrieve_docs(user_query)
        response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        #fixed_response = "Hi, this is a fixed response!"
        st.chat_message("AI Lawyer").write(response)
    
    else:
        st.error("I Need a Handbook to uphold law!")