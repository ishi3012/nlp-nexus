import re
import string
from typing import List

class RetainOption(Enum):
    URLS = auto()
    HTML = auto()
    PUNCTUATION = auto()
    EMAIL = auto()
    USERNAME = auto()

def clean_text(text: str, retain: List[RetainOption] = []) -> str:
    """
    Cleans the input text by removing specified elements unless they are mentioned to  be retained.

    Parameters:
    - text (str)                    : The input text to clean
    - retain (List[RetainOption])   : A list of elements to retain. Options include RetainOption.URLS, RetainOption.HTML, RetainOption.PUNCTUATION, RetainOption.EMAIL,RetainOption.USERNAME

    Returns: 
    - str                           : The cleaned text    

    """
    pass