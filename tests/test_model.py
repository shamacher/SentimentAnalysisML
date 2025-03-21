from app.model import analyze_sentiment


def test_analyze_sentiment():
    assert analyze_sentiment('This is great!') == 'positive'
    assert analyze_sentiment('This is terrible.') == 'negative'
    assert analyze_sentiment('This is okay.') == 'neutral'
