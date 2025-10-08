"""Streamlit UI template
This template is non-functional until backend is implemented.
"""
import streamlit as st

st.title("Document RAG Chatbot (Template)")
st.info("Core features are not implemented in this template. See ISSUES.md.")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    for f in uploaded_files:
        st.write(f.name)

query = st.text_input("Ask a question")
if st.button("Ask"):
    st.warning("ask_question is not implemented in this template.")
