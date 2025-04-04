import streamlit as st
import os
import base64
from ocr_engine import extract_text_from_image
from nlp_engine import extract_information
from validation import validate_policy_data
from PyPDF2 import PdfReader

st.title("Insurance Policy Analyzer")

policy_type = st.selectbox("Insurance Policy Type", ["Auto Insurance", "Home Insurance", "Health Insurance", "Life Insurance"])

uploaded_file = st.file_uploader("Upload Policy Document", type=["pdf", "jpg", "png"])

if uploaded_file is not None:
    file_data = uploaded_file.read()
    file_ext = uploaded_file.name.split(".")[-1]

    # Extract text from PDF or image
    if file_ext == 'pdf':
        try:
            reader = PdfReader(uploaded_file)
            text = "".join(p.extract_text() for p in reader.pages)
        except Exception as e:
            st.error(f"Error extracting text from PDF: {e}")
            text = None
    else:
        # Save the image to a temporary file
        with open("temp_image." + file_ext, "wb") as f:
            f.write(file_data)
        try:
            text = extract_text_from_image("temp_image." + file_ext)
            os.remove("temp_image." + file_ext)
        except Exception as e:
            st.error(f"Error extracting text from image: {e}")
            text = None

    if text:
        # Extract information using NLP
        try:
            doc = extract_information(text)
        except Exception as e:
            st.error(f"Error extracting information using NLP: {e}")
            doc = None

        # Validate policy data
        try:
            is_valid, message = validate_policy_data(text)
        except Exception as e:
            st.error(f"Error validating policy data: {e}")
            is_valid = False
            message = "Validation failed"

        st.write("## Analysis Results")
        st.write(f"**Policy Type:** {policy_type}")
        st.write(f"**OCR Text:** {text}")
        if doc:
            st.write(f"**NLP Data:** {doc}")
        st.write(f"**Validation Status:** {is_valid}")
        st.write(f"**Validation Message:** {message}")
