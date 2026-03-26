import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Fake Job Detector", page_icon="🔍")

st.title("🔍 Smart Fake Job Detection System")
st.write("This model uses Machine Learning to predict if a job is Fake or Real.")

# Sample dataset (you can expand later)
data = {
    "text": [
        "Earn money fast without experience pay registration fee",
        "Work from home and earn 5000 daily limited seats",
        "Complete forms or pay penalty data entry job",
        "Urgent hiring no interview click here apply",
        "Software engineer job at Infosys with interview process",
        "Marketing executive required with 2 years experience",
        "Hiring data analyst with salary and benefits",
        "Walk in interview for sales executive tomorrow"
    ],
    "label": [1, 1, 1, 1, 0, 0, 0, 0]  # 1 = Fake, 0 = Real
}

df = pd.DataFrame(data)

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
model = LogisticRegression()
model.fit(X, df["label"])

# Input
user_input = st.text_area("Enter Job Description or Link")

if st.button("Check Job"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        prob = model.predict_proba(input_vector)[0]

        if prediction == 1:
            st.error(f"❌ Fake Job (Confidence: {round(prob[1]*100, 2)}%)")
        else:
            st.success(f"✅ Real Job (Confidence: {round(prob[0]*100, 2)}%)")

# Footer
st.markdown("---")
st.write("⚠️ Accuracy improves with more data.")
