# Smart Contract Assistant

This is a modular RAG (Retrieval-Augmented Generation) application built to analyze and answer questions about legal contracts.

## Features
- **Modular Structure:** The code is cleanly divided into data ingestion and retrieval modules.
- **Langchain Integration:** Fully utilizes Langchain for document processing, embeddings, and vector stores.
- **Interactive UI:** User-friendly web interface powered by Gradio.

## Setup Instructions

**1. Clone the repository:**
`git clone <Your-GitHub-Repo-Link-Here>`
`cd Smart-Contract-Assistant`

**2. Install dependencies:**
Make sure you have Python installed, then run:
`pip install -r requirements.txt`

**3. Environment Variables:**
Create a `.env` file in the root directory and add your Groq API key:
`GROQ_API_KEY="your_api_key_here"`

**4. Run the application:**
`python app.py`