import re
import string
import emoji
from enum import Enum, auto
from nltk.corpus import stopwords
import pandas as pd
from typing import List

# # Ensure NLTK stopwords are downloaded
# nltk.download('stopwords')


# Define stopwords
STOPWORDS = set(stopwords.words('english'))

class RetainOption(Enum):
    URLS = auto()
    HTML = auto()
    PUNCTUATION = auto()
    EMAIL = auto()
    USERNAME = auto()
    NUMBERS = auto()
    NON_ASCII = auto()
    STOP_WORDS = auto()
    EMOJIS = auto()


def clean_text(series: pd.Series, retain: List[RetainOption] = []) -> pd.Series:
    """
    Cleans the input text by removing specified elements unless they are mentioned to  be retained.

    Parameters:
    - series (pd.series)            : Pandas series containing text data
    - retain (List[RetainOption])   : A list of elements to retain. (e.g. URLS, HTML)

    Returns: 
    - series (pd.series)            : Pandas Series with cleaned text   

    """

    # precompile regex patterns for efficiency
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    html_pattern = re.compile(r'<.*?>')
    punctuation_pattern = re.compile(r'[^\w\s]')
    number_pattern = re.compile(r'\d+')
    email_pattern = re.compile(r'\S+@\S+')
    non_ascii_pattern = re.compile(r'[^\x00-\x7F]+')
    
    emoji_pattern = re.compile("[" 
                                 u"\U0001F600-\U0001F64F"  # emoticons
                                 u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                 u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                 u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                 u"\U00002702-\U000027B0"
                                 u"\U000024C2-\U0001F251"
                                 "]+", flags=re.UNICODE)
    whitespace_pattern = re.compile(r'\s+')

    if not retain:
        print("No patterns to retain. Processing all patterns.")
        patterns_to_process = set(RetainOption.__members__)
    else:
        patterns_to_process = set(RetainOption.__members__) - set(retain)

    # Clean the text data
    for pattern in patterns_to_process:
        
        if pattern == "URLS":
            series = series.str.replace(url_pattern, '',regex = True)

        if pattern == "HTML":
            series = series.str.replace(html_pattern, '', regex = True)            

        if pattern == "PUNCTUATION":
            series = series.str.replace(punctuation_pattern, '', regex = True)

        if pattern == "NUMBERS":
            series = series.str.replace(number_pattern, '', regex = True)

        if pattern == "EMAIL":
            series = series.str.replace(email_pattern, '', regex = True)

        if pattern == "NON_ASCII":
            series = series.str.replace(non_ascii_pattern, '', regex = True)

        if pattern == "EMOJIS":
            series = series.str.replace(emoji_pattern, '', regex = True)    
    
    series = series.str.lower()

    # Remove stop words
    if not retain or RetainOption.STOP_WORDS not in retain:
        series = series.apply(lambda x: ' '.join(word for word in x.split() if word not in STOPWORDS))

    # Strip and remove white spaces
    series = series.str.strip()
    series = series.str.replace(whitespace_pattern, ' ', regex = True)

    return series

# if __name__ == "__main__":
#     data = {
#         'review' : [
#             "I love this product! 😊 It's amazing! https://example.com",
#             "This is the worst purchase I have made. 😡 Contact me at email@example.com",            
#         ]
#     }
#     df = pd.DataFrame(data)
#     cleaned_data = clean_text(df['review'], retain = [RetainOption.URLS,RetainOption.EMAIL])
#     #cleaned_data = clean_text(df['review'], retain = [])
#     print(cleaned_data)