import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def query_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    with httpx.AsyncClient(timeout=60.0) as client:
        response = client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["response"]