import nltk

# Check if 'punkt' is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    print("Punkt tokenizer is installed.")
except LookupError:
    print("Punkt tokenizer is not installed.")
    nltk.download('punkt')

# Check if 'stopwords' is downloaded
try:
    nltk.data.find('corpora/stopwords')
    print("Stopwords are installed.")
except LookupError:
    print("Stopwords are not installed.")
    nltk.download('stopwords')
