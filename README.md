# Sensitive Data Detection & Compliance Assistant

## Overview

This project is an AI-powered application that allows users to upload documents and automatically detect sensitive or confidential information. The application classifies the document based on its risk level, generates a compliance and security summary using AI, and allows users to ask questions about the uploaded document.

This project is developed as a simple prototype to demonstrate document processing, AI integration, and basic compliance analysis.

---

# Features

## Document Upload

Supports the following file formats:

- PDF (.pdf)
- TXT (.txt)
- CSV (.csv)

---

## Sensitive Data Detection

The application detects sensitive information using Regular Expressions (Regex), including:

- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers
- Credit Card Numbers
- Bank Account Numbers
- API Keys
- Passwords
- Employee IDs

---

## Risk Classification

Based on the number of sensitive items detected, the document is classified as:

- Low Risk
- Medium Risk
- High Risk

---

## AI-Generated Compliance Summary

Using the Groq API with an open-source Large Language Model, the application generates:

- Compliance observations
- Security risks
- Suggested remediation steps

---

## Question Answering

Users can ask questions about the uploaded document, for example:

- What sensitive data exists in this document?
- How many email addresses are present?
- Summarize this document.
- What compliance risks are identified?

---

# Project Structure

```
Sensitive-Data-Detection/

│── app.py
│── detector.py
│── utils.py
│── ai_helper.py
│── requirements.txt
│── README.md
│── .env
│
├── uploads/
│
└── sample_files/
    │── sample.txt
    │── sample.csv
    └── sample.pdf
```

---

# Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3 (via Groq)
- Pandas
- PyPDF2
- Regular Expressions (Regex)
- python-dotenv

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Sensitive-Data-Detection.git

cd Sensitive-Data-Detection
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Groq API Key

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can obtain a free API key from:

https://console.groq.com/keys

---

## 5. Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# How It Works

1. Upload a PDF, TXT, or CSV document.
2. Extract text from the uploaded file.
3. Detect sensitive information using Regex.
4. Classify the document risk level.
5. Send the extracted text to the Groq API to generate:
   - Compliance observations
   - Security risks
   - Remediation suggestions
6. Ask questions about the uploaded document using AI.

---

# Architecture Overview

```
                User Uploads Document
                        │
                        ▼
              Text Extraction Module
                        │
                        ▼
        Sensitive Data Detection (Regex)
                        │
                        ▼
          Risk Classification Module
                        │
                        ▼
             Groq Large Language Model
          ┌──────────────┴──────────────┐
          ▼                             ▼
 Compliance Summary          Question Answering
          │
          ▼
      Streamlit User Interface
```

---

# AI / ML Approach Used

This application combines rule-based detection with an AI-powered language model.

### Sensitive Data Detection

Regular Expressions (Regex) are used to identify structured sensitive information such as:

- Aadhaar Numbers
- PAN Numbers
- Email Addresses
- Phone Numbers
- Credit Card Numbers
- Passwords
- API Keys
- Employee IDs

Regex provides fast and accurate detection for structured patterns.

### AI-Based Analysis

The Groq API is used to access the Llama 3 language model for:

- Document summarization
- Compliance observations
- Security risk identification
- Remediation recommendations
- Interactive question answering

This hybrid approach combines deterministic pattern matching with natural language understanding.

---

# Challenges Faced

Some challenges encountered during development include:

- Supporting multiple document formats.
- Extracting readable text from PDFs.
- Designing Regex patterns for different types of sensitive information.
- Combining deterministic detection with AI-generated insights.
- Building a simple prototype while satisfying all assignment requirements.

---

# Future Improvements

Potential future enhancements include:

- OCR support for scanned documents.
- Automatic data masking and redaction.
- Multi-document analysis.
- Retrieval-Augmented Generation (RAG) using FAISS or ChromaDB.
- Audit logging.
- User authentication.
- Dashboard with analytics.
- Docker containerization.
- Cloud deployment.

---

# Sample Questions

Examples of questions users can ask:

- What sensitive information exists in this document?
- How many email addresses are present?
- Summarize this document.
- What compliance risks are identified?
- Are there any passwords in this document?
- List all PAN numbers.
- What is the overall risk level?

---

# Deployment

The application can be deployed using:

- Streamlit Community Cloud
- Render
- Railway

Deployment Link:

```
https://your-app.streamlit.app
```

---

# Demo Video

The demonstration video (2–5 minutes) should include:

- Uploading a document
- Sensitive data detection
- Risk classification
- AI-generated compliance summary
- Question answering

---

# Author

**Anurag V S**


GitHub:
https://github.com/zeepriozz

LinkedIn:
https://www.linkedin.com/in/anurag-v-s-106226269

---

# License

This project is developed for educational purposes and interview assessment only.
