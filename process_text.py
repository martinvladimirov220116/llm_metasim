import os
import requests
import logging
from pathlib import Path
import spacy

# --- Setup logging ---
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define paths and constants
INPUT_PATH = Path("input_text/b2b_extracted_text.txt")
OUTPUT_PATH = Path("output_text/cleaned_output.txt")
API_URL = "http://localhost:8000/clean_text"
CHUNK_SIZE = 800  # max characters per chunk


def split_text_to_chunks(text, max_chunk_length=CHUNK_SIZE):
    logging.info("Splitting text into chunks...")
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    logging.info(f"Total chunks created: {len(chunks)}")
    return chunks


def clean_chunk(chunk, index):
    try:
        logging.info(f"Cleaning chunk {index + 1}...")
        response = requests.post(API_URL, json={"text": chunk})
        response.raise_for_status()
        return response.json()["cleaned_text"]
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error cleaning chunk {index + 1}: {e}")
        return ""


def process_document():
    os.makedirs(OUTPUT_PATH.parent, exist_ok=True)

    logging.info(f"Reading from {INPUT_PATH}")
    with open(INPUT_PATH, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = split_text_to_chunks(text)

    cleaned_chunks = []
    for i, chunk in enumerate(chunks):
        cleaned_text = clean_chunk(chunk, i)
        cleaned_chunks.append(cleaned_text)

    logging.info(f"Writing cleaned output to {OUTPUT_PATH}")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n\n".join(cleaned_chunks))

    logging.info("✅ Done! Document processed successfully.")


if __name__ == "__main__":
    process_document()
