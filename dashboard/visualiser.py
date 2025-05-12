import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_distortion_counts(distortion_counter):
    df = pd.DataFrame.from_dict(distortion_counter, orient='index', columns=['Count'])
    df = df.sort_values(by='Count', ascending=False).reset_index().rename(columns={'index': 'Distortion'})
    fig = px.bar(df, x='Distortion', y='Count', title="Cognitive Distortion Frequency")
    fig.show()

def plot_emotion_trends(emotion_df):
    fig = px.line(emotion_df, x=emotion_df.index, y=emotion_df.columns, title="Weekly Emotion Trends")
    fig.show()

def plot_entry_frequency(freq_series):
    plt.figure(figsize=(10, 4))
    freq_series.plot(kind='bar')
    plt.title("Journal Entry Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Entries")
    plt.tight_layout()
    plt.show()
