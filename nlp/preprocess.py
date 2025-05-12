import re

def clean_text(text: str) -> str:
    """
    Cleans text by removing extra whitespace, emojis, and unwanted characters.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)                # Remove extra spaces
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII (like emojis)
    return text.lower()

def split_sentences(text: str) -> list:
    """
    Splits input into sentences (optional for analyzing parts).
    """
    return re.split(r'[.?!]\s+', text)