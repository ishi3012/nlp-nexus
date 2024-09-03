# Data Preprocessing Module

The NLP Nexus preprocessing module helps with cleaning, encoding, embedding, and tokenizing raw text data, preparing it for machine learning models.

## Available Functions

- **clean_text(text)**: Cleans raw text by removing URLs, punctuation, and special characters.
- **encode_labels(labels)**: Encodes categorical labels into numeric format.
- **tokenize_text(text)**: Tokenizes text into individual words using NLTK.
- **bert_tokenize(text, pretrained_model='bert-base-uncased')**: Tokenizes text using a pre-trained BERT tokenizer.- 
- **generate_word_embeddings(sentences)**: Generates word embeddings using the Word2Vec algorithm.
- **sentence_to_embedding(sentence, model)**: Converts a sentence to a fixed-size vector by averaging word embeddings.
