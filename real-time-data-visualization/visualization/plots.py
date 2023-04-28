python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_tweet_count(df):
    """
    Plot the number of tweets over time

    :param df: pandas DataFrame containing tweet data
    """
    # Convert the date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Resample the data to get the number of tweets per hour
    df = df.resample('H', on='Date').count()
    
    # Plot the tweet count over time
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Text'])
    ax.set(title='Number of tweets over time', xlabel='Time', ylabel='Number of tweets')
    st.pyplot(fig)

    
def plot_tweet_sentiment(df):
    """
    Plot the sentiment of tweets over time

    :param df: pandas DataFrame containing tweet data
    """
    # Convert the date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Group the data by date and sentiment
    df = df.groupby(['Date', 'Sentiment']).size().reset_index(name='Count')
    
    # Pivot the data to create a wide-format DataFrame with one column for each sentiment
    df = df.pivot(index='Date', columns='Sentiment', values='Count')
    
    # Fill in any missing values with zero
    df = df.fillna(0)
    
    # Normalize the data to get the percentage of each sentiment
    df = df.div(df.sum(axis=1), axis=0) * 100
    
    # Plot the sentiment of tweets over time
    fig, ax = plt.subplots()
    sns.lineplot(data=df)
    ax.set(title='Sentiment of tweets over time', xlabel='Time', ylabel='% of tweets')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    st.pyplot(fig)
