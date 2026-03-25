import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🎬", layout="centered")

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        truncation=True,
        max_length=512
    )

classifier = load_model()

st.title("🎬 Movie Review Sentiment Analyzer")
st.markdown("Enter a movie review and find out if it's positive or negative.")

review = st.text_area("Your review:", placeholder="e.g. This movie was absolutely fantastic...", height=150)

if st.button("Analyze →", type="primary"):
    if not review.strip():
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            result = classifier(review)[0]

        label = result['label']
        score = result['score']

        if label == "POSITIVE":
            st.success(f"👍 **POSITIVE** — confidence: {score:.2%}")
        else:
            st.error(f"👎 **NEGATIVE** — confidence: {score:.2%}")

        st.progress(score)

        st.markdown("---")
        st.caption("Model: DistilBERT fine-tuned on SST-2")

st.markdown("---")
st.markdown("**Example reviews to try:**")
st.markdown("- *This movie was absolutely fantastic! Best film I've seen in years.*")
st.markdown("- *Terrible film. Boring plot, bad acting. Complete waste of time.*")
st.markdown("- *Not bad. Not good either. Passable way to spend an afternoon.*")
