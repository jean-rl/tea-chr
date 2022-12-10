from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def main():
    # Load article abstracts
    abstracts = pd.read_csv("../../data/jair.csv")

    # Load topic model
    topic_model = BERTopic.load("../../models/topic_model")

    # Find topics in the abstracts
    topics, _ = topic_model.transform(abstracts["abstract"])

    # List to save the topics keywords
    keywords = list()
    for topic in set(topics):
        keywords.append([t[0] for t in topic_model.get_topic(topic)])

    # Save the topics keywords
    pd.DataFrame(keywords).to_csv("../../data/topic_keywords.csv", index=False, header=False)


if __name__ == "__main__":
    main()