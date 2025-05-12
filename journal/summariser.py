from transformers import pipeline
import pandas as pd

class Summarizer:
    def __init__(self, entries_df):
        # Initialize Hugging Face's summarization pipeline with BART or T5
        self.summarizer = pipeline("summarization")
        self.entries_df = entries_df

    def generate_summary(self):
        # Combine journal entries from the past week (or select last n entries)
        recent_entries = self.entries_df.tail(7)  # Get last 7 entries (one week)
        journal_text = "\n".join(recent_entries['entry'].values)

        # Summarize the journal entries using the Hugging Face model
        summary = self.summarizer(journal_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        return summary
