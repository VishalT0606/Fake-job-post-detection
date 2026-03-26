import streamlit as st

st.set_page_config(page_title="Fake Job Detector", page_icon="🔍")

st.title("🔍 Fake Job Detection System")
st.write("Enter job description or job link to check if it's Fake or Real.")

# Input box
user_input = st.text_area("Paste Job Description or Link here")

# Simple keyword-based detection
def detect_fake_job(text):
    fake_keywords = [
        "earn money fast",
        "no experience required",
        "pay registration fee",
        "work from home and earn",
        "urgent hiring no interview",
        "click here to apply",
        "limited seats hurry",
        "investment required"
    ]

    score = 0
    text = text.lower()

    for word in fake_keywords:
        if word in text:
            score += 1

    if score >= 2:
        return "❌ This job looks FAKE"
    else:
        return "✅ This job seems REAL"

# Button
if st.button("Check Job"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        result = detect_fake_job(user_input)
        st.subheader(result)

# Footer
st.markdown("---")
st.write("⚠️ This is a basic demo. Not 100% accurate.")
