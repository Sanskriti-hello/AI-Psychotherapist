import pandas as pd
import os
from datetime import datetime

class EntryHandler:
    def __init__(self, file_path='journal_entries.csv'):
        self.file_path = file_path
        self.load_entries()

    def load_entries(self):
        if os.path.exists(self.file_path):
            self.entries_df = pd.read_csv(self.file_path)
        else:
            self.entries_df = pd.DataFrame(columns=["date", "entry", "mood", "tags"])

    def save_entry(self, entry_text, mood=None, tags=None):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = {
            "date": date_str,
            "entry": entry_text,
            "mood": mood or "neutral",
            "tags": tags or []
        }
        self.entries_df = self.entries_df.append(new_entry, ignore_index=True)
        self.entries_df.to_csv(self.file_path, index=False)
        print(f"Entry saved: {date_str}")

    def get_entries(self):
        return self.entries_df
