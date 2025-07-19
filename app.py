
!pip install transformers streamlit

import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

summarizer = load_summarizer()

st.title("Simple Text Summarizer")

text_to_summarize = st.text_area("Enter the text you want to summarize:")

if st.button("Summarize"):
    if text_to_summarize:
        with st.spinner("Summarizing..."):
            summary = summarizer(text_to_summarize, max_length=150, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")

st.info("This app uses the facebook/bart-large-cnn model from Hugging Face Transformers for summarization.")
    