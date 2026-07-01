import pandas as pd
from PyPDF2 import PdfReader

def extract_text(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        pdf = PdfReader(uploaded_file)
        text = ""

        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

        return text

    elif filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.to_string()

    return ""