from django.test import TestCase
from .models import Sentiment

class SentimentModelTest(TestCase):
    def test_should_save_sentiment(self):
        Sentiment.objects.create(text = 'pop', value = False)

        actual = Sentiment.objects.last()

        self.assertEqual('pop', actual.text)
        self.assertEqual(False, actual.value)

