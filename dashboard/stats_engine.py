import pandas as pd
from collections import Counter
from datetime import datetime

class StatsEngine:
    def __init__(self, journal_df):
        """
        journal_df must contain: ['timestamp', 'text', 'emotions', 'distortions']
        'emotions' and 'distortions' should be lists per entry
        """
        self.df = journal_df.copy()
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])

    def distortion_stats(self):
        all_distortions = [d for sublist in self.df['distortions'] for d in sublist]
        return Counter(all_distortions)

    def emotion_stats_over_time(self, freq='W'):
        """
        Returns average emotion score counts per week
        (requires 'emotions' to be dicts like {'sad': 0.9, 'joy': 0.1})
        """
        emotion_df = self.df.copy()
        emotion_df['timestamp'] = pd.to_datetime(emotion_df['timestamp'])

        # Explode emotions into separate columns
        expanded = emotion_df['emotions'].apply(pd.Series)
        expanded['timestamp'] = emotion_df['timestamp']
        return expanded.groupby(pd.Grouper(key='timestamp', freq=freq)).mean()

    def entry_frequency(self, freq='D'):
        return self.df.groupby(pd.Grouper(key='timestamp', freq=freq)).size()
