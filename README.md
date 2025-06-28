# LLM Interaction Suite with Ollama (Mistral)

This project is a 3-task pipeline that demonstrates interaction with a locally hosted Large Language Model (LLM) using [Ollama](https://ollama.com/) and the `mistral` model. It includes a backend service (FastAPI) and two applications — one for document cleaning and another for conversational interaction.

---

## Technologies Used

- **FastAPI**: For creating API endpoints.
- **Ollama**: To run LLM models locally (tested with `mistral`).
- **Python 3.13**
- **SpaCy**: For sentence-level tokenization.
- **Uvicorn**: To serve the FastAPI app.
- **httpx**: Used in the backend (`llm_client.py`) for making asynchronous HTTP calls to the local Ollama API, enabling non-blocking LLM queries.

---

## Project Structure

```plaintext
llm_metasim/
├── main.py               # FastAPI backend that connects to Ollama
├── llm_client.py         # Handles the actual call to Ollama's local API
├── process_text.py       # Task 2: Cleans a noisy text document via FastAPI
├── conversation.py       # Task 3: Command-line app simulating a seller-buyer conversation
├── input_text/
│   └── b2b_extracted_text.txt  # Noisy input document
├── output_text/
│   └── cleaned_output.txt      # Cleaned version of the text
└── README.md
```
---

## Tasks Overview

**Task 1:** API for Text Cleaning and Chat
Implemented with FastAPI.

Two endpoints:

/clean_text – Removes headers, footers, and other noise from input text.

/chat – Continues a conversation history, acting as a picky buyer.

Calls query_ollama() in llm_client.py, which sends prompts to Ollama running locally.

**Task 2:** Batch Document Cleaning
- Reads a large text document.

- Splits it into sentence-preserving chunks (max 800 characters).

- Sends each chunk to /clean_text endpoint.

- Saves the cleaned text to output_text/cleaned_output.txt.

**Task 3:** Buyer/Seller Interactive Chat

- CLI interface (conversation.py).

- Simulates a conversation between a human seller (user input) and an LLM buyer.

- Stores the history of the chat 

- Ends when the user types "Bye".

- Messages are exchanged via the /chat endpoint.


## LLM Setup

- Install Ollama: https://ollama.com

- Pull a model: ollama pull mistral

- Start Ollama server: ollama serve

## How To Run

- Start the FastAPI backend (Task 1): uvicorn main:app --reload

- Run Task 2 (Document Cleaning): python process_text.py

- Run Task 3 (Buyer/Seller Chat): python conversation.py

## Notes
All LLM interactions are local via Ollama's API.

Project was developed on Windows 10 Pro - Version	2009 - OS Build	19045.5965

Conversations and cleaning rely entirely on prompts sent to the mistral model.

Execution speed will vary on CPU vs GPU. (This project was developed on CPU.)

Some portions of this project (llm_client.py, parts of conversation.py, parts of process_text.py) were developed with help from ChatGPT to increase productivity, fix bugs, and improve structure. Everything ChatGPT answer has been checked and corrected if necessary, so that it suits the project.

## Author
**Martin Vladimirov**
