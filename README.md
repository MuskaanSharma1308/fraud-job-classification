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

## 🔹 Dataset & Features

### Text Features
Combined all major text fields into one column:  

- Job title  
- Job description  
- Requirements  
- Benefits  
- Company profile  

Transformed using **TF-IDF** to capture:  
- Important words  
- Scam patterns  
- Suspicious phrases like *“no interview”*, *“immediate joining”*  

### Numeric & Categorical Features
- Telecommuting  
- Employment type  
- Required education & experience  
- Industry & function  
- Location  

Boolean fields converted to `0/1` for model learning.  

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
- Handles **high-dimensional data efficiently**, which is important for text features  
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
