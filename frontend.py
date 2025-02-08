import streamlit as st
from main import answer_quer , retrieve_docs , llm_model

uploaded_file = st.file_uploader("Upload PDF",
                                 type = "pdf",
                                 accept_multiple_files=False
                                 )

user_query = st.text_area("Enter your prompt" , height=150 , placeholder="Ask Anything")

ask_question = st.button("Ask AI")

if ask_question:

    if uploaded_file:
        st.chat_message("user").write(user_query)
        retrieve_docs = retrieve_docs(user_query)
        response = answer_quer(documents = retrieve_docs , model=llm_model , query=user_query)
        st.chat_message("AI Answer").write(response)

else:
    st.error("Kindly upload a valid pdf")