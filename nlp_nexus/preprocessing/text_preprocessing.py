import re
import nltk

nltk.download('punkt')


class TextPreprocessor:
    """
    A base class text preprocessing that implements the common cleaning methods. 
    The class can be extended by NLP tasks to implement custom preprocessing steps. 

    Methods:

        remove_html_tags(): TextPreprcessor
            Removes HTML tags from the text.
        
        remove_special_characters(): TextPreprocessor
            Removes special characters from the text, leaving only alphanumeric characters. 

        lowercase() : TextPreprocessor
            Converts all chararcters in the text to lowercase. 

        remove_stopwords(stopwords_list: list): TextPreprocessor
            Removes the stopwords from the text using the provided list.

        tokenize(tokenizer: str) : TextPreprocessor
            Tokenizes the text using the specified tokenizer.
        
        get_cleaned_text(): str
            Returns the cleaned text after all preprocessing is done.
    
    """

    def __init__(self, text: str):
        """
        Initializes the TextPreprocessor with the input text.

        Parameters:
            - text : str
                The input text to be preprocessed. 
        """

        self.text = text

    def remove_html_tags(self):
        """
        Removes HTML tags from the text. 

        Returns:
            TextPreprocessor : self
            Returns the instance of the class containing the text with no HTML tags
        """
        #r'<.*?>'

        self.text = re.sub(r'<.*?>', '', self.text)

        return self


if __name__ == "__main__":

    sample_text = "Welcome to NLP-Nexus! Visit <a href='example.com'>our site</a> for more info."

    processor = TextPreprocessor(sample_text)

    print(f"Input Text   = {sample_text}")
    print(f"Cleaned Text = {processor.remove_html_tags().text}")

