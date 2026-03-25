# 🎬 Sentiment Analysis of Movie Reviews

🚀 **[Live Demo](https://ktarnowski17-sentiment-analysis-app-egi7fm.streamlit.app)**

This project focuses on sentiment analysis of movie reviews from the IMDB dataset.
The goal was to automatically classify whether a movie review is positive or negative.
I tested two approaches — a simple TF-IDF baseline and a pretrained DistilBERT — to find the best solution for this task.

---

## 📁 Dataset
IMDb Movie Reviews from HuggingFace Datasets
- 25,000 training reviews
- 25,000 test reviews
- Balanced: 50% positive / 50% negative

---

## 📌 What I did
In this project, I tested two different approaches:
- Logistic Regression with TF-IDF
- Pretrained DistilBERT model

I wanted to see how a simple baseline compares to a more advanced NLP model.

---

## 🧠 Models

### Logistic Regression + TF-IDF
- basic text cleaning
- removing stopwords
- converting text into numerical features using TF-IDF
- fast and simple model

### DistilBERT (pretrained)
- model: `distilbert-base-uncased-finetuned-sst-2-english`
- used with Hugging Face pipeline
- no additional training (only predictions)

---

## 📊 Results

| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Logistic Regression | 0.88 | 0.88 |
| DistilBERT | 0.89 | 0.89 |

### Observations
- DistilBERT performed slightly better
- Logistic Regression is much faster and easier to use
- Transformer model handles more complex sentences better

### Key takeaway
A simple TF-IDF model achieves nearly the same accuracy as a transformer but trains 50x faster.
For production use cases where speed matters, Logistic Regression would be the better choice.

---

## 🔍 Error Analysis
I checked some incorrect predictions and noticed:
- Logistic Regression struggles with:
  - sarcasm
  - longer and more complex sentences
- DistilBERT performed slightly better in some of these cases, although the overall difference between models is small
- Both models struggle with mixed or unclear sentiment

---

## 📂 Project Structure
```
sentiment_analysis/
├── analizaopinii.ipynb  ← main analysis notebook
├── app.py               ← Streamlit web app
├── requirements.txt
└── README.md
```
---

## ⚙️ Tools and Libraries
- Python
- pandas, numpy
- scikit-learn
- transformers (Hugging Face)
- matplotlib / seaborn
- Streamlit

---

## 🚀 How to run

1. Clone the repository:
```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the web app:
```bash
streamlit run app.py
```
