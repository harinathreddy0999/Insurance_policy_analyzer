from flask import Flask, request, jsonify
import os
import logging
from ocr_engine import extract_text_from_image
from nlp_engine import extract_information
from validation import validate_policy_data
from PyPDF2 import PdfReader
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/upload', methods=['POST'])
def upload_policy():
    logging.info("Upload policy endpoint hit")
    if 'file' not in request.files:
        logging.error("No file uploaded")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    policy_type = request.form.get('policyType')
    logging.info(f"Policy type: {policy_type}")

    if file.filename == '':
        logging.error("No file selected")
        return jsonify({'error': 'No file selected'}), 400

    if file:
        filename = file.filename
        file_data = request.form.get('file')
        logging.info(f"File data: {file_data[:100]}...") # Log first 100 characters
        header = file_data.split(',', 1)[0]
        logging.info(f"Header: {header}")

        # Determine the file extension
        if header.startswith('data:application/pdf'):
            file_ext = '.pdf'
        elif header.startswith('data:image/jpeg'):
            file_ext = '.jpg'
        elif header.startswith('data:image/png'):
            file_ext = '.png'
        else:
            logging.error("Invalid file type")
            return jsonify({'error': 'Invalid file type'}), 400

        # Extract text from PDF or image
        if file_ext == '.pdf':
            try:
                #with open(file_path, 'rb') as f:
                #    reader = PdfReader(f)
                #    text = "".join(p.extract_text() for p in reader.pages)
                text = "PDF Extraction not yet implemented"
            except Exception as e:
                logging.exception("Error extracting text from PDF")
                return jsonify({'error': 'Error extracting text from PDF'}), 500
        else:
            try:
                #text = extract_text_from_image(file_path)
                text = "Image Extraction not yet implemented"
            except Exception as e:
                logging.exception("Error extracting text from image")
                return jsonify({'error': 'Error extracting text from image'}), 500

         # Extract information using NLP
        try:
            doc = extract_information(text)
        except Exception as e:
            logging.exception("Error extracting information using NLP")
            return jsonify({'error': 'Error extracting information using NLP'}), 500

        return jsonify({
            'message': 'File uploaded and processed successfully',
            'policy_type': policy_type,
            'file_data': file_data
        })

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True, port=5005)
