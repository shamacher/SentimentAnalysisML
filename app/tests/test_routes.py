import pytest
from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_analyze_sentiment_positive(client):
    response = client.post('/sentiment/analyze', json={'text': 'This is great'})
    assert response.status_code == 200
    assert response.json['sentiment'] == 'positive'


def test_analyze_sentiment_negative(client):
    response = client.post('/sentiment/analyze', json={'text': 'This is terrible'})
    assert response.status_code == 200
    assert response.json['sentiment'] == 'negative'
