from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
def classify_emotion(text: str) -> dict:
    """
    Returns a dict of emotion probabilities.
    Example output: {'sadness': 0.45, 'joy': 0.10, 'anger': 0.05, ...}
    """
    results = classifier(text)[0]
    return {res['label']: res['score'] for res in results}