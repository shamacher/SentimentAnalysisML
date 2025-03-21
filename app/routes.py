from flask_restx import Namespace, Resource, fields
from .model import analyze_sentiment


ns = Namespace('sentiment', description='Sentiment analysis operations')

sentiment_model = ns.model('Sentiment', {'text': fields.String(required=True,
                                                               description='Text to analyze')
                                         })


@ns.route('/analyze')
class SentimentAnalysis(Resource):
    @ns.expect(sentiment_model)
    @ns.doc('analyze_sentiment')
    def post(self):
        text = ns.payload['text']
        sentiment = analyze_sentiment(text)
        return {'sentiment': sentiment}
