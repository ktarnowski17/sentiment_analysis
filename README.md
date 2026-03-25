# Sentiment Analysis on IMDb Reviews

## What is this project?
This is my second data science project where I analyzed movie reviews from IMDb and built models to predict whether a review is positive or negative.

## What I did
- Explored the dataset (50,000 reviews) — checked class distribution, review lengths, most common words
- Cleaned the text — removed HTML tags, punctuation, stopwords
- Built two models and compared them:
  - TF-IDF + Logistic Regression (simple and fast)
  - DistilBERT (transformer-based, more advanced)

## Results
| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Logistic Regression | 88.10% | 88.11% |
| DistilBERT | 89.07% | 88.75% |

Interesting finding — the simple model performs almost as well as the transformer, but trains in 30 seconds instead of 25 minutes. Both models struggled with sarcastic and mixed-sentiment reviews.

## Tech used
Python, pandas, scikit-learn, HuggingFace Transformers, matplotlib, wordcloud

## Dataset
IMDb dataset from HuggingFace (25k train / 25k test)
