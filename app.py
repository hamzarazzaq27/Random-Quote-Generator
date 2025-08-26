import streamlit as st
import random

st.title("💡 Random Quote Generator")

# List of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Happiness depends upon ourselves. – Aristotle",
    "Turn your wounds into wisdom. – Oprah Winfrey",
]

if st.button("✨ Generate Quote"):
    st.info(random.choice(quotes))
