Document RAG Chatbot (SLoP 5.0 - Backend)

Welcome to the official Document RAG Chatbot project for SLoP 5.0, the open source contribution competition conducted by GDGC DAU!

About SLoP 5.0

SLoP (Semester Long Open source Projects) 5.0 is a flagship open source contribution competition organized by GDGC DAU. Participants contribute to real-world projects, collaborate, and learn open source workflows by solving curated issues and submitting pull requests.

Competition: SLoP 5.0
Organizer: GDGC DAU
Project Category: Backend / AI
Project Name: Document RAG Chatbot

Project Overview

Document RAG Chatbot is a simple, extensible, open source chatbot designed to answer questions from multiple PDFs using LangChain RAG, HuggingFace embeddings, and FAISS.

The current version provides:

Streamlit-based UI for PDF upload and querying

Placeholder modules for PDF ingestion, embedding, and retrieval

All core modules are currently placeholders. Contributors are expected to implement:

PDF loading & text extraction

Text chunking and embedding

FAISS vectorstore creation and querying

LangChain RAG question-answering

Streamlit UI integration

How to Participate

Fork this repository and clone your fork.

Pick an open issue (see the Issues tab) or suggest a new feature.

Discuss your approach in the issue comments if needed.

Create a branch for your fix/feature.

Submit a Pull Request referencing the issue.

Wait for review and feedback!

Getting Started (Local Development)
git clone <your-fork-url>
cd document-rag-chatbot
pip install -r requirements.txt
cp .env.example .env
streamlit run src/ui/app_streamlit.py


Open http://localhost:8501
 in your browser.

Note: This is the empty-template version. The chatbot is non-functional until core modules are implemented. See ISSUES.md for tasks.

Features & Contribution Opportunities

PDF upload (template implemented)

Ask a question (template implemented)

PDF ingestion pipeline (to be implemented by contributors)

Text chunking & metadata storage (to be implemented)

Embeddings using HuggingFace (to be implemented)

FAISS vectorstore build & query (to be implemented)

LangChain RAG QA chain (to be implemented)

Streamlit UI enhancements (to be implemented)

Optional Gradio interface (to be implemented)

All core logic currently raises NotImplementedError. Your task is to implement these features!

Guidelines

Follow the CONTRIBUTING.md for coding standards and PR process.

Be respectful and collaborative in discussions and reviews.

Ask questions if you are unsure about requirements or implementation.

License

This project is open source and available under the MIT License.

Happy hacking and good luck in SLoP 5.0!

For any queries, reach out via the Issues tab or contact the GDGC DAU organizers.