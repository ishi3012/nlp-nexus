import re
import string
import emoji
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from typing import List
from enum import Enum, auto

class LanguageOption(Enum):
    ENGLISH = auto()

# Ensure necessary NLTK data is available
def ensure_nltk_data():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)


class TextPreprocessor:
    """
    A class used to preprocess text for NLP tasks, offering options for 
    cleaning, tokenization, stemming, lemmatization and handling stopwords.

    Attributes:
    - enable_stemming (bool)         : If True, apply stemming to the tokens after tokenization.
    - enable_lemmatization (bool)    : If True, apply lemmatization to the tokens after tokenization.
    - exclude_stopwords (bool)       : If True, stopwords will be removed from the tokens.
    - stemmer (PorterStemmer)        : A stemmer object to perform stemming. (Default Porter Stemmer).
    - lemmatizer (WordLemmatizer)    : A lemmatizer object to perform lemmatization.
    
    """

    def __init__(self, enable_stemming = False, enable_lemmatization = False, exclude_stopwords = True):

        """
        Initializes the TextPreprocessor class with given options for stemming,
        lemmatization, and stopword removal.

        Parameters:

        - enable_stemming (bool)         : Option to apply stemming. Default is False.
        - enable_lemmatization (bool)    : Option to apply Lemmatization. Default is False.
        - exclude_stopwords (bool)       : Option to remove stopwords . Default is True.  

        """
        # Ensure NLTK data is available when the class is instantiated
        ensure_nltk_data() 

        self._enable_stemming = enable_stemming
        self._enable_lemmatization = enable_lemmatization
        self._exclude_stopwords = exclude_stopwords

        # Initialize stemmer and lemmatizer

        self._stemmer = PorterStemmer()
        self._lemmatizer = WordNetLemmatizer()

    def _clean_text(self, series: pd.Series) -> pd.Series:

        """
        Private method: Removes HTML tags, URLS, Emails, Punctuations, Numbers, NonASCII, Emojis

        Parameters:

        - series (pd.Series)      : A Pandas series containing the text data to be cleaned.
        
        Returns:

        - pd.Series               : A Pandas series containing the cleaned text. 

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
    
    def _remove_punctuation(self, series: pd.Series) -> pd.Series:

        """
        Private method: Removes punctuation from text in the input series.

        Parameters:

            - series (pd.Series)    : A Pandas series that contains the text data from which punctuation marks need to be removed.

        Returns:

            - pd.Series             : A Pandas series that contains text with no punctuation marks. 

        """
        # precompile regex pattern
        punctuation_pattern = re.compile(r'[^\w\s]')

        # Remove punctuation marks

        series = series.str.replace(punctuation_pattern, '', regex = True)

        return series
    
    def _remove_numbers(self,series: pd.Series) -> pd.Series:

        """
        Private method: Removes numbers from the text in the input series.
        
        Parameters:

            - series (pd.Series)    : A Pandas series that contains the text data from which numbers need to be removed.

        Returns:

            - pd.Series    : A Pandas series that contains text with no numbers. 

        """
        # precompile regex pattern
        number_pattern = re.compile(r'\d+')

        # Remove numbers

        series = series.str.replace(number_pattern, '', regex = True)

        return series
    
    def _tokenize_words(self, series: pd.Series) -> pd.Series:

        """
        Private method: Tokenizes the text in the input series into words.

        Parameters: 

            - series (pd.Series)      : A Pandas series containing the text data to be tokenized.

        Returns:

            - pd.Series      : A Pandas series where each entry is a list of word tokens.
        """
        series = series.apply(word_tokenize)

        return series
    
    def _remove_stopwords(self, tokenized_series: pd.Series, language: LanguageOption = LanguageOption.ENGLISH) -> pd.Series:
        """
        Private method: Removes stop words from the tokenized text in the input Pandas series.

        Parameters:

            - tokenized_series (pd.Series)  : A Pandas series where each entry is a list of word tokens.
            - language(LanguageOption)      : The language of the stopwords (default is 'english')
        
        Returns:
            -  pd.Series                    : A Pandas Series where stopwords have been removed from the input series.
        """
        if language != LanguageOption.ENGLISH:
            raise ValueError(f"Unsupported language '{LanguageOption.ENGLISH}'. Only 'english' is currently supported.")
        
        stop_words = set(stopwords.words('english'))

        series = tokenized_series.apply(lambda tokens : [word for word in tokens if word not in stop_words])

        return series
    
    def _stem_words(self, tokenized_series: pd.Series) -> pd.Series:

        """
        Private method: Applies stemming to the tokenized text in the input series using the PorterStemmer.

        Parameters:
            
            - tokenized_series (pd.Series)      : A Pandas series where each entry is a list of word tokens.

        Returns:
            
            - pd.Series                         : A Pandas series where each word in the tokens is stemmed. 
        """

        series = tokenized_series.apply(lambda tokens: [self._stemmer.stem(word) for word in tokens])

        return series

    def _lemmatize_words(self, tokens_series: pd.Series) -> pd.Series:
        """
        Private method: Applies lemmatization to the tokenized text in the input series using the WordNetLemmatizer.

        Parameters:
        ----------
        tokens_series : pd.Series
            A pandas Series where each entry is a list of word tokens.

        Returns:
        -------
        pd.Series
            A pandas Series where each word in the tokens is lemmatized.
        """
        return tokens_series.apply(lambda tokens: [self._lemmatizer.lemmatize(word) for word in tokens])

    def preprocess_text(self, series: pd.Series) -> pd.Series:

        """
        Public method: Preprocesses the text in a pandas Series by applying lowercasing, cleaning, 
        punctuation and number removal, tokenization, stopword removal, and optionally stemming/lemmatization.

        Parameters:
        ----------
        series : pd.Series
            A pandas Series containing the text data to be preprocessed.

        Returns:
        -------
        pd.Series
            A pandas Series where each entry is a list of preprocessed word tokens.
        """
        series = self._clean_text(series)
        series = self._remove_punctuation(series)
        series = self._remove_numbers(series)
        tokens = self._tokenize_words(series)

        if self._exclude_stopwords:
            tokens = self._remove_stopwords(tokens)

        if self._enable_stemming:
            tokens = self._stem_words(tokens)

        if self._enable_lemmatization:
            tokens = self._lemmatize_words(tokens)
        
        return tokens


if __name__ == "__main__":

    #Create sample dataset 
    data = {'text':["I love NLP, 2345! https://d2l.depaul.edu/ 😍", "This is a3 great to3ol! ishishiv3012@gmail.com", "Natural Language Processing is fun."]}
    df = pd.DataFrame(data)

    # Instantiate the preprocessor
    preprocessor = TextPreprocessor(enable_stemming=True, enable_lemmatization = True, exclude_stopwords = True)

    # Preprocess the text column in the dataframe
    df['processed_text'] = preprocessor.preprocess_text(df['text'])

    # Show the dataframe with preprocessed text
    print(df)
    
    
        

        



