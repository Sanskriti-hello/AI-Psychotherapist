import streamlit as st
from agents.cbt_agent import CBTAgent
from journal.entry_handler import load_entries, save_entry
from dashboard.visualizer import plot_distortion_counts, plot_emotion_trends
from dashboard.stats_engine import StatsEngine
from journal.summarizer import summarize_weekly

agent = CBTAgent()

st.set_page_config(layout="wide", page_title="AI CBT Therapist")
st.sidebar.title("🧠 AI CBT App")
mode = st.sidebar.radio("Choose Mode", ["Chat", "Journal", "Dashboard"])

if mode == "Chat":
    st.title("💬 Talk to the CBT Therapist")
    user_input = st.text_input("What's on your mind today?")
    if st.button("Send"):
        response = agent.chat(user_input)
        st.markdown(f"**Therapist:** {response}")

elif mode == "Journal":
    st.title("📔 Daily Reflection")
    journal_text = st.text_area("Write your thoughts:")
    if st.button("Save Entry"):
        save_entry(journal_text)
        st.success("Journal saved!")

elif mode == "Dashboard":
    st.title("📊 Your Cognitive Patterns")
    entries = load_entries()
    stats = StatsEngine(entries)
    distortion_counts = stats.distortion_stats()
    plot_distortion_counts(distortion_counts)
