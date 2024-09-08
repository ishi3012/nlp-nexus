import pytest
import pandas as pd
from nlp_nexus.preprocessing.text_cleaning import clean_text, RetainOption

@pytest.fixture
def test_data():
    return {
        'review' : [
            #"I love this product! 😊 It's amazing! https://example.com",
            "This is the worst purchase I have made. 😡 Contact me at email@example.com",
            #"Check out our website at www.example.com for more details.",
            "12345 is a number, and this is an emoji 🎉",
            #"<html><body>HTML content</body></html>",
            #"Non-ASCII characters: café, naïve, jalapeño."
        ]
    }

def test_basic_cleaning(test_data):
    df = pd.DataFrame(test_data)
    cleaned_series = clean_text(df['review'])
    
    expected_series = pd.Series([
        #"love product amazing",
        "worst purchase made contact",
        #"check website details",
        "number emoji",
        #"html content",
        #"Non-ASCII characters: cafe, naive, jalapeno."
    ], name="review")

    pd.testing.assert_series_equal(cleaned_series, expected_series)
    
