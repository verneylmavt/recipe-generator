# setup_nlp.py
import nltk
import spacy

def download_nltk_models():
    print("Downloading NLTK models...")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    print("NLTK models downloaded successfully.")

def download_spacy_model():
    print("Downloading spaCy 'en_core_web_sm' model...")
    spacy.cli.download("en_core_web_sm")
    print("spaCy model downloaded successfully.")

if __name__ == "__main__":
    download_nltk_models()
    download_spacy_model()