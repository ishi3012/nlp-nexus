from setuptools import setup, find_packages
from setuptools.command.install import install
import nltk

# class PostInstallCommand(install):
#     """Post-installation for downloading NLTK stopwords."""
#     def run(self):
#         install.run(self)
#         # Download NLTK data
#         nltk.download('punkt')
#         nltk.download('stopwords')
#         nltk.download('wordnet')

setup(
    name="nlp-nexus",
    version="0.1.0",
    author="Shilpa Musale",
    author_email="ishishiv3012@gmail.com",
    description="A portfolio of advanced NLP projects including sentiment analysis, question answering, conversational agents, and more.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ishi3012/nlp-nexus",
    packages=find_packages(
        include=[
            'Sentiment-Analysis',
            'Question-Answering',
            'ChatGPT-Conversational-Agent',
            'Machine-Translation',
            'Text-Summarization',
            'nlp_nexus'
        ]
    ),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scikit-learn>=1.0.0',
        'tensorflow>=2.6.0',
        'torch>=1.10.0',
        'transformers>=4.11.0',
        'matplotlib>=3.4.0',
        'nltk>=3.6.0',
        'emoji>=1.5.0',
        'spacy>=3.0.0',
        'emoji==2.0.0',
        'pytest==7.0.0',
        'textblob>=0.15.3'
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    extras_require={
        'dev': [
            'pytest>=6.2.0',
            'sphinx>=4.0.0',
            'tox>=3.24.0',
            'coverage>=5.5'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
