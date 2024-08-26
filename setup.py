from setuptools import setup, find_packages

setup(
    name="nlp_nexus",
    version="0.1.0",
    description="NLP Nexus: A collection of advanced NLP projects.",
    author="Shilpa Musale",
    author_email="ishishiv3012@gmail.com",
    url="https://github.com/ishi3012/nlp-nexus",
    packages=find_packages(include=["sentiment_analysis", "question_answering", "chatgpt_agent", "machine_translation", "text_summarization"]),
    include_package_data=True,
    install_requires=[
        "numpy>=1.23.1",
        "pandas>=1.5.1",
        "scikit-learn>=1.1.1",
        "nltk>=3.7",
        "flask>=2.2.3",
        "tensorflow>=2.9.1",
        "transformers>=4.20.1",
        "torch>=1.11.0",  
    ],
    extras_require={
        "dev": ["pytest>=7.1.2", "black>=22.3.0", "flake8>=4.0.1"],
    },
    entry_points={
        "console_scripts": [
            "train-sentiment=sentiment_analysis.train:main",
            "evaluate-sentiment=sentiment_analysis.evaluate:main",
            "train-qa=question_answering.train:main",
            "evaluate-qa=question_answering.evaluate:main",
            
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
