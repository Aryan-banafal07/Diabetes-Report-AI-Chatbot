# Diabetes Report AI Chatbot

## Description:
The **Diabetes Report AI Chatbot** is an interactive Streamlit-based application designed to analyze diabetes-related medical reports (in PDF format) using AI models. It processes the uploaded PDF reports, extracts the relevant data, and presents key insights related to diabetes management. The chatbot provides structured, easy-to-read outputs with bolded key findings and conclusions. 

This app leverages LangChain and Ollama for Natural Language Processing (NLP), as well as FAISS for efficient vector storage and retrieval of document embeddings. It can be used for reading medical reports, interpreting lab test results, and answering user queries based on the report.

## Features:
- **PDF Report Upload**: Upload any diabetes-related medical report in PDF format.
- **Natural Language Querying**: Ask questions related to the report and receive AI-driven responses.
- **Key Insights Extraction**: Automatically generate structured insights based on the uploaded report, focusing on diabetes management and related tests.
- **Formatted Output**: The output is well-structured and clearly formatted with bolded key findings and conclusions.

## Installation Instructions:

### Prerequisites:
- Python 3.7+ 
- Virtual environment (optional but recommended)

### Steps to Install:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/diabetes-report-chatbot.git
    cd diabetes-report-chatbot
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/MacOS
    .\.venv\Scripts\activate  # For Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Make sure you have access to the Ollama model, as this app requires it for querying.

### Requirements:
- **LangChain**: A framework for building language model applications.
- **Ollama**: A local model to process queries and generate answers from documents.
- **Streamlit**: For building the web interface.
- **PyPDFLoader**: For loading and extracting text from PDF documents.
- **FAISS**: For vector storage and retrieval.

## Usage:

1. Start the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the application in your browser. You will be prompted to upload a diabetes-related medical report (in PDF format).

3. Once the report is uploaded, the app will analyze the content and provide key insights regarding the diabetes tests mentioned in the report, including any lab results such as Urinalysis, ESR, and Thyroid function.

4. You can also ask specific questions related to the report, and the chatbot will respond accordingly.

5. The output is displayed in a structured and readable format, with key findings and conclusions highlighted.

---

### Example Output:

**Key Findings:**

1. **No signs of diabetes:**  
   Based on the information provided in the report, there are no findings that suggest the presence of diabetes.

2. **Urinalysis and thyroid function tests:**
   - Both tests are within **normal limits**, which does not indicate the presence of diabetes.

3. **Erythrocyte Sedimentation Rate (ESR) Test:**
   - **ESR**: 21 mm/hr (Normal range: 6-12 mm/hr).  
   - This result suggests there is no **inflammation** in the body that could be indicative of diabetes.

4. **Thyroid Function Test:**
   - **Triiodothyronine (T3 Total)**: 0.83 ng/mL (Normal range: 0.7-2.04 ng/mL).  
   - **Thyroid Stimulating Hormone (TSH)**: 1.033 µIU/mL (Normal range: 0.4-5.5 µIU/mL).  
   - These results suggest **no thyroid dysfunction** that could be related to diabetes.

**Conclusion:**
Based on the urinalysis and thyroid function tests, **no evidence of diabetes** has been found. However, it is important to note that these results do not rule out diabetes entirely, and **further testing** may be required for a definitive diagnosis.

Contact
For questions or feedback, please contact  [(https://aryanbanafal.vercel.app)] or aryanbanafal7@gmai.com.
