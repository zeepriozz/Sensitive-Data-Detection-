import streamlit as st

from utils import extract_text
from detector import detect_sensitive_data, classify_risk
from ai_helper import ask_ai

st.title("Sensitive Data Detection & Compliance Assistant")

uploaded = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt", "csv"]
)

if uploaded:

    text = extract_text(uploaded)

    st.subheader("Document Preview")

    st.text_area("", text[:3000], height=200)

    results, total = detect_sensitive_data(text)

    st.subheader("Sensitive Data")

    if results:

        for key, values in results.items():

            st.write(f"### {key}")

            for v in values:
                st.write(v)

    else:

        st.success("No Sensitive Data Found")

    risk = classify_risk(total)

    st.subheader("Risk Classification")

    st.error(risk)

    st.subheader("Compliance Summary")

    summary = ask_ai(

        text,

        """
Generate:

1. Compliance observations

2. Security risks

3. Remediation steps

"""

    )

    st.write(summary)

    st.subheader("Ask Questions")

    question = st.text_input("Ask anything")

    if st.button("Ask"):

        answer = ask_ai(text, question)

        st.write(answer)