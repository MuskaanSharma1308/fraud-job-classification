# 🕵️ Fraudulent Job Posting Detection (ML + NLP)

Detect fraudulent job postings automatically using **Machine Learning** and **Natural Language Processing**.  

---

## 🔹 Why This Project?

Fake job postings are everywhere — some look almost real, making them risky.  
This project is designed to **identify fraudulent jobs before they reach users**, prioritizing **catching fraud effectively**.  

---

## 🔹 Features

- Predicts whether a job posting is:  
  ✅ **Genuine**  
  🚨 **Fraudulent**  
- Shows **prediction confidence**  
- Analyzes both **text content** and **job metadata**  

---

## 🔹 Dataset

The dataset used for this project is too large to host on GitHub.  
You can download it directly from Kaggle:

[Real or Fake Job Posting Prediction Dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)

**Dataset includes:**  
- **Text features:** job title, job description, requirements, benefits, company profile  
- **Metadata features:** telecommuting, employment type, required education & experience, industry, function, location  

> After downloading, save the CSV file in your project folder to run the app.  

---

## 🔹 Data Preprocessing

- Removed irrelevant or highly missing columns  
- Cleaned and merged text fields  
- Encoded categorical data numerically  
- Handled class imbalance using `class_weight`  
- Saved trained objects (`model.pkl`, `tfidf.pkl`) for deployment  

---

## 🔹 Models Used

### Logistic Regression
- Selected because it works **very well with TF-IDF text data**  
- **Fast and interpretable** — you can see which features influence predictions  
- Handles **high-dimensional data efficiently**  
- Provides **class probabilities** for transparency in prediction confidence  

### Random Forest
- Captures complex feature interactions  
- Performs well with mixed feature types  
- Helps understand **feature importance**  

> Both models were evaluated, compared, and validated.  

---

## 🔹 Prediction Examples

- "Congratulations! Please transfer the security amount to confirm."  
  → 🚨 Fraudulent  

- "We are hiring a Software Developer. Apply with resume and portfolio."  
  → ✅ Genuine  

---

## 🔹 Deployment

- Streamlit app accepts **job description input**  
- Shows **prediction** and **confidence scores**  
- Trained objects saved:  
  - `model.pkl`  
  - `tfidf.pkl`  

---

## 🔹 How to Run

```bash
# Clone the repo
git clone <your-repo-url>
cd Job-Fraud-Detection

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

