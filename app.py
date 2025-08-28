import streamlit as st
from transformers import pipeline

st.title("📝 Smart Text Summarization")

st.write("Write a full text")

# ورودی متن
text_input = st.text_area("Enter your text here", height=300)

if st.button("summarize"):

    if not text_input.strip():
        st.warning("Please enter the text first.")
    else:
        with st.spinner("Processing... please wait"):
            # بارگذاری مدل خلاصه‌سازی
            summarizer = pipeline("summarization")

            # گرفتن خلاصه متن (میتونی max_length/min_length رو تنظیم کنی)
            summary = summarizer(text_input, max_length=130, min_length=30, do_sample=False)

            st.success("✅ خلاصه متن:")
            st.write(summary[0]['summary_text'])
else:
    st.info("Enter your text and click the 'Summarize' button.")
