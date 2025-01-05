import os
import streamlit as st
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from transformers import pipeline, AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import numpy as np


st.title('NEWS Research Tool')
st.sidebar.title("News Articles URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL{i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = 'store.pkl'

main_placeholder = st.empty()


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")


def embed_with_retry_hf(documents, retries=5, delay=2):
    for attempt in range(retries):
        try:
            texts = [doc.page_content for doc in documents]
            embeddings = embedding_model.encode(texts, convert_to_tensor=False)
            return embeddings
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (2 ** attempt)) 
            else:
                raise e

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading Started....")
    data = loader.load()
    if not data:
        st.error("No data was loaded from the URLs. Please ensure the URLs are valid.")
        st.stop()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000,
        chunk_overlap=100
    )
    main_placeholder.text("Text Splitting Started.....")
    docs = text_splitter.split_documents(data)
    if not docs:
        st.error("Document splitting failed. No valid text was extracted for embedding.")
        st.stop()

    main_placeholder.text("Embedding Started.....")

    try:
        embeddings = embed_with_retry_hf(docs)
        if embeddings is None or len(embeddings) == 0:
            st.error("Embedding process failed. No embeddings were generated.")
            st.stop()
        with open(file_path, "wb") as f:
            pickle.dump((docs, embeddings), f)
    except Exception as e:
        st.error(f"Error during embedding: {e}")
        st.stop()


query = main_placeholder.text_input("Question:")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            docs, embeddings = pickle.load(f)
            texts = [doc.page_content for doc in docs]
            query_embedding = embedding_model.encode([query], convert_to_tensor=False)[0]
            similarities = np.dot(embeddings, query_embedding) / (
                np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
            )
            top_indices = similarities.argsort()[-3:][::-1]
            top_docs = [texts[i] for i in top_indices]
            try:
                answers = []
                for doc in top_docs:
                    result = qa_pipeline(question=query, context=doc)
                    answers.append(result)

                st.header("Answer")
                if answers:
                    best_answer = max(answers, key=lambda x: x['score'])
                    st.write(best_answer['answer'])

                    st.subheader("Sources:")
                    for idx, doc in enumerate(top_docs):
                        st.write(f"Source {idx + 1}: {doc[:200]}...")
                else:
                    st.write("No answer found.")
            except Exception as e:
                st.error(f"Error during querying: {e}")
