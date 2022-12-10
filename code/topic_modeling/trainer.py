from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def main():
    # Load article abstracts
    abstracts = pd.read_csv("../../data/jair.csv")

    # Remove stopwords
    vectorizer = CountVectorizer(stop_words="english")

    # Create a BERTopic model
    topic_model = BERTopic(language="english", verbose=True, nr_topics=None, vectorizer_model=vectorizer)

    # Find topics in the abstracts
    topics, _ = topic_model.fit_transform(abstracts["abstract"])

    # Save model
    topic_model.save("../../models/topic_model")

    print('Model saved!')


if __name__ == "__main__":
    main()