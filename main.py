import os
import streamlit as st
import pdfplumber
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import pandas as pd
import re

# Load the diabetes report (PDF)
def load_diabetes_report(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
    return pages

# Convert the text from the PDF into embeddings and store them in FAISS
def create_vector_db(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    documents = [Document(page_content=page) for page in pages]
    chunks = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model="mistral")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

# Ask questions related to the diabetes report
def ask_question(db, question):
    retriever = db.as_retriever()
    llm = OllamaLLM(model="mistral", temperature=0.5)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    answer = qa_chain.invoke(question)
    return answer.get("result", "No information found.")

# Extract and summarize key diabetes parameters
def extract_parameters(db):
    parameters = {
        "HbA1c (%)": "What is the HbA1c level mentioned in the report?",
        "Fasting Glucose (mg/dL)": "What is the fasting glucose level mentioned in the report?",
        "Postprandial Glucose (mg/dL)": "What is the postprandial glucose level mentioned in the report?",
        "Cholesterol (mg/dL)": "What is the cholesterol level mentioned in the report?",
        "Triglycerides (mg/dL)": "What is the triglyceride level mentioned in the report?",
        "Blood Pressure (mmHg)": "What is the blood pressure mentioned in the report?"
    }

    extracted_values = {param: ask_question(db, query) for param, query in parameters.items()}

    abnormal_parameters = {}
    reference_ranges = {
        "HbA1c (%)": (5.7, 6.5),
        "Fasting Glucose (mg/dL)": (70, 125),
        "Postprandial Glucose (mg/dL)": (70, 180),
        "Cholesterol (mg/dL)": (0, 200),
        "Triglycerides (mg/dL)": (0, 150),
        "Blood Pressure (mmHg)": (90, 120)
    }

    formatted_results = []
    for param, value in extracted_values.items():
        match = re.search(r"\d+\.?\d*", value)
        numeric_value = float(match.group(0)) if match else None

        if numeric_value is not None:
            lower, upper = reference_ranges.get(param, (None, None))
            status = "Normal" if lower <= numeric_value <= upper else "**Abnormal**"
            formatted_results.append((param, numeric_value, status))

            if status == "**Abnormal**":
                abnormal_parameters[param] = numeric_value
        else:
            formatted_results.append((param, "Not Found", "N/A"))

    return formatted_results, abnormal_parameters

# Generate insights from the report
def generate_insights(db):
    insights = ask_question(db, "Provide detailed diabetes management insights based on this report.")
    return insights

# Streamlit UI
def main():
    st.title("🩺 Diabetes Report AI Chatbot")
    st.markdown("### Upload your Diabetes Report (PDF) to analyze key health metrics and get AI-powered insights.")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        with open("diabetes_report.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        pages = load_diabetes_report("diabetes_report.pdf")
        db = create_vector_db(pages)

        st.success("✅ Report loaded successfully! You can now ask questions, generate insights, or view a summarized report.")

        question = st.text_input("🔍 Ask a question related to the report:")
        if question:
            response = ask_question(db, question)
            st.markdown(f"### **Answer:**\n{response}")

        if st.button("📊 Summarized Report"):
            formatted_results, abnormal_params = extract_parameters(db)
            
            st.markdown("### 📌 **Key Diabetes Parameters**")
            df = pd.DataFrame(formatted_results, columns=["Parameter", "Value", "Status"])
            st.dataframe(df)

            if abnormal_params:
                st.markdown("### ⚠️ **Abnormal Parameters Detected**")
                for param, value in abnormal_params.items():
                    st.markdown(f"🔴 **{param}: {value}**")

        if st.button("💡 Generate Insights"):
            insights = generate_insights(db)
            st.markdown("### 📜 **Diabetes Management Insights**")
            st.write(insights)

    st.markdown("*📌 Disclaimer: This chatbot is for informational purposes only and should not be used as a substitute for professional medical advice.*")

if __name__ == "__main__":
    main()
