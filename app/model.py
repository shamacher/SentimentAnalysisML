import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['pos'] > sentiment_scores['neg'] and \
            sentiment_scores['pos'] > sentiment_scores['neu']:
        return 'positive'
    elif sentiment_scores['neg'] > sentiment_scores['pos'] and \
            sentiment_scores['neg'] > sentiment_scores['neu']:
        return 'negative'
    else:
        return 'neutral'
