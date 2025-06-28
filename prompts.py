def build_cleaning_prompt(text: str) -> str:
    return f"""Clean the following text by removing artifacts like headers, footers, and page numbers:\n\n{text}"""

def build_chat_prompt(history: list[str]) -> str:
    return "\n".join(history) + "\nAI:"