#import streamlit as st
#import pickle

# load tfidf
#with open("tfidf_vectorizer.pkl", "rb") as f:
#    tfidf = pickle.load(f)

# load model
#with open("fraud_model.pkl", "rb") as f:
   # model = pickle.load(f)

#st.title("Job Fraud Detection")

#text = st.text_area("Enter job description")

##if st.button("Predict"):
    #X = tfidf.transform([text])
   # pred = model.predict(X)[0]

    #if pred == 1:
     #   st.write("Fraudulent Job")
    #else:
       # st.write("Genuine Job")
import streamlit as st
import pickle

# load tfidf
with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# load model
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Job Fraud Detection")

text = st.text_area("Enter job description")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a job description")
    else:
        X = tfidf.transform([text])

        # prediction
        pred = model.predict(X)[0]

        # probability
        prob = model.predict_proba(X)[0]
        real_prob = prob[0]
        fraud_prob = prob[1]

        # result (simplified)
        if pred == 1:
            st.write("🚨 Fraudulent Job")
        else:
            st.write("✅ Genuine Job")

        # probability display
        st.subheader("Prediction Confidence")
        st.write(f"Genuine Job: **{real_prob:.2f}**")
        st.write(f"Fraudulent Job: **{fraud_prob:.2f}**")
