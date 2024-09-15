import re
import pandas as pd 
from nlp_nexus.preprocessing.text_preprocessing import TextPreprocessor
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BertTokenizer
from spellchecker import SpellChecker
import contractions



class SentimentAnalysisPreprocessor(TextPreprocessor):

    """
    A class to perform text preprocessing for the sentiment-analysis task.
    This class extends the bsic text preprocessing by including:
        - Normalization
        - Handling negations
        - Emoji and sland handling 
        - Feature extraction
    """

    def __init__(self, use_bert = False):

        """
        Initialize the SentimentAnalysisPreprocessor class.

        : param use_bert : Boolean flag to use BERT embeddings (default is False)
        """

        super().__init__()
        self.use_bert = use_bert


        if use_bert:
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            self.bertmodel = BertModel.from_pretrained('bert-base-uncased')

    def correct_spelling(self, series: pd.Series) -> pd.Series:
        
        """
        Correct spelling mistakes in each text string of a pandas series.

        Parameters:

            - series (pd.Series)    : A Pandas series that contains text strings with potential spelling mistakes.

        Returns:

            - pd.Series             : A Pandas series with corrected spellings. 

        """
        if not isinstance(series, pd.Series):
            raise ValueError("Input must be a pandas Series.")
        
        # Define a function to correct spellings in the text string
        def correct_spelling_text(text):
            if isinstance(text, str):
                spell = SpellChecker()
                words = text.split()
                corrected_text = ' '.join([spell.candidates(word).pop() if len(spell.candidates(word)) > 0 else word for word in words])
                return corrected_text
            return text  # Return the original text if it's not a string

        # Apply spelling correction to each text string in the pandas series
        corrected_text = series.apply(correct_spelling_text)

        return corrected_text
    
    def normalize_text(self, series: pd.Series) -> pd.Series:

        """
        Normalized a pandas series of text byexpanding contractions and correcting spellings. 

        Parameters:

            - series (pd.Series)    : A Pandas series that contains text strings with potential spelling mistakes and contractions (e.g. don't).

        Returns:

            - pd.Series             : A Pandas series with normalized text strings.

        """

        if not isinstance(series, pd.Series):
            raise ValueError("Input must be a pandas Series.")
        
        normalized_text = series.apply(lambda text: contractions.fix(text) if isinstance(text, str) else text)
        corrected_text = self.correct_spelling(normalized_text)
        return corrected_text


if __name__ == "__main__":

     preprocessor = SentimentAnalysisPreprocessor()
     
     data = pd.Series (["I don't haev this pne"])
     print(preprocessor.normalize_text(data))

    