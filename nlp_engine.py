import spacy

nlp = spacy.load("en_core_web_sm")

def extract_information(text):
    doc = nlp(text)
    # Add your NLP logic here to extract relevant information
    # For example, you can extract entities, keywords, etc.
    return doc
