import re
import string
import emoji
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


class TextPreprocessor:
    """
    A class used to preprocess text for NLP tasks, offering options for 
    cleaning, tokenization, stemming, lemmatization and handling stopwords.

    Attributes:
    - enable_stemming (bool)         : If True, apply stemming to the tokens after tokenization.
    - enable_lemmatization (bool)    : If True, apply lemmatization to the tokens after tokenization.
    - remove_stopwords (bool)        : If True, stopwords will be removed from the tokens.
    - stemmer (PorterStemmer)        : A stemmer object to perform stemming. (Default Porter Stemmer).
    - lemmatizer (WordLemmatizer)    : A lemmatizer object to perform lemmatization.
    
    """

    def __init__(self, enable_stemming = False, enable_lemmatization = False, remove_stopwords = True):

        """
        Initializes the TextPreprocessor class with given options for stemming,
        lemmatization, and stopword removal.

        Parameters:

        - enable_stemming (bool)         : Optionn to apply stemming. Default is False.
        - enable_lemmatization (bool)    : Option to apply Lemmatization. Default is False.
        - remove_stopwords (bool)        : Option to remove stopwords . Default is True.  

        """

        self.enable_stemming = enable_stemming
        self.enable_lemmatization = enable_lemmatization
        self.remove_stopwords = remove_stopwords

        # Initialize stemmer and lemmatizer

        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, series: pd.Series) -> pd.Series:

        """
        Removes HTML tags, URLS, Emails, Punctuations, Numbers, NonASCII, Emojis

        Parameters:

        - series (pd.Series)      : A Panda series containing the text data to be cleaned.
        
        Returns:

        - series (pd.Series)      : A Panda series containing the cleaned text. 

        """

        # precompile regex patterns for efficiency
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        html_pattern = re.compile(r'<.*?>')        
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

        series = series.str.replace(url_pattern, '',regex = True)  # Remove URLs
        series = series.str.replace(html_pattern, '', regex = True) # Remove HTML
        series = series.str.replace(email_pattern,'',regex = True) # Remove email ids
        series = series.str.replace(non_ascii_pattern, '', regex = True) # Remove non-ascii characters
        series = series.str.replace(emoji_pattern,'',regex = True) # Remove emojis
        series = series.str.replace(whitespace_pattern, ' ', regex = True) # Remove Whitespace

        # Remove extra spaces in the beginning and end of the text.
        series = series.str.strip()

        # Convert text in the input sequence to lowercase.
        series = series.str.lower()
        
        return series
    
    def remove_punctuation(self, series: pd.Series) -> pd.Series:

        """
        Removes punctuation from text in the input series.

        Parameters:

            - series (pd.Series)    : A Panda series that contains the text data from which punctuation marks need to be removed.

        Returns:

            - series (pd.series)    : A Panda series that contains text with no punctuation marks. 

        """
        # precompile regex pattern
        punctuation_pattern = re.compile(r'[^\w\s]')

        # Remove punctuation marks

        series = series.str.replace(punctuation_pattern, '', regex = True)

        return series
    
    def remove_numbers(self,series: pd.Series) -> pd.Series:

        """
        Removes numbers from the text in the input series.
        
        Parameters:

            - series (pd.Series)    : A Panda series that contains the text data from which numbers need to be removed.

        Returns:

            - series (pd.series)    : A Panda series that contains text with no numbers. 

        """
        # precompile regex pattern
        number_pattern = re.compile(r'\d+')

        # Remove numbers

        series = series.str.replace(number_pattern, '', regex = True)

        return series
    
    # def tokenize_words(self, series: pd.Series) -> pd.Series:

    #     """

    #     """


if __name__ == "__main__":

    #Create sample dataset 
    data = {'text':["I love NLP, 2345! https://d2l.depaul.edu/ 😍", "This is a3 great to3ol! ishishiv3012@gmail.com", "Natural Language Processing is fun."]}
    df = pd.DataFrame(data)

    preprocessor = TextPreprocessor()

    cleanedText = preprocessor.clean_text(df["text"])
    cleanedText = preprocessor.remove_punctuation(cleanedText)
    cleanedText = preprocessor.remove_numbers(cleanedText)

    print(cleanedText)
        

        



