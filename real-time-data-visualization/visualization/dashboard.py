
import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('../data/tweets.csv')

# Define sidebar widgets
st.sidebar.title("Filters")
filter_by = st.sidebar.selectbox("Filter by:", ["All", "Positive", "Negative", "Neutral"])

# Filter data
if filter_by == "Positive":
    data = data[data.sentiment == "positive"]
elif filter_by == "Negative":
    data = data[data.sentiment == "negative"]
elif filter_by == "Neutral":
    data = data[data.sentiment == "neutral"]

# Define main content widgets
st.title("Real-time Data Visualization Dashboard")
st.write(f"Number of tweets: {len(data)}")

with st.beta_expander("View Data"):
    st.write(data)

with st.beta_expander("Sentiment Distribution"):
    sentiment_counts = data.sentiment.value_counts()
    st.bar_chart(sentiment_counts)

with st.beta_expander("Top 10 Hashtags"):
    hashtags = {}
    for tweet in data.text:
        if "#" in tweet:
            for word in tweet.split():
                if word.startswith("#"):
                    if word.lower() in hashtags:
                        hashtags[word.lower()] += 1
                    else:
                        hashtags[word.lower()] = 1
    top10 = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)[:10]
    st.bar_chart(pd.DataFrame(top10, columns=["Hashtag", "Count"]).set_index("Hashtag"))

