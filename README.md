# 🎬 Sentiment Analysis of Movie Reviews

This project focuses on sentiment analysis of movie reviews from the IMDB dataset.  
The goal was to compare a simple machine learning approach with a pretrained transformer model.

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
|------|--------|---------|
| Logistic Regression | 0.88 | 0.88 |
| DistilBERT | 0.89 | 0.89 |

### Observations:
- DistilBERT performed slightly better
- Logistic Regression is much faster and easier to use
- Transformer model handles more complex sentences better

---

## 🔍 Error Analysis

I checked some incorrect predictions and noticed:

- Logistic Regression struggles with:
  - sarcasm
  - longer and more complex sentences

- DistilBERT performed slightly better in some of these cases, although the overall difference between models is small

- Both models struggle with mixed or unclear sentiment

---

## ⚙️ Tools and Libraries

- Python
- pandas, numpy
- scikit-learn
- transformers (Hugging Face)
- matplotlib / seaborn

---

## 🚀 How to run

1. Clone the repository:
```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
