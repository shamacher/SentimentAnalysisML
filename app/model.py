import nltk
from nltk.sentiment import SentimentIntesnityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntesnityAnalyzer()


def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05:
        return 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'
