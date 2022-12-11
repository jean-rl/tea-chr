from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os
from cleantext import clean
import time

USE_CUDA = True

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
if USE_CUDA:
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
else:
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


def train_topic_model(data, size, savepath):
    start_time = time.time()

    # Check if there are any missing values
    print("Checking for missing values...")
    print(data.isnull().sum())

    # Remove missing values
    if data.isnull().sum().sum() > 0:
        print("Removing missing values...")
        print("Removed instances:", data.isnull().sum().sum())
        data.dropna(inplace=True)
        print("New number of instances:", len(data))
    else:
        print("No missing values found.")

    # Select some instances for training
    abstracts = data.sample(frac=size, random_state=42)["abstract"].tolist()
    print("Instance count:", len(abstracts))

    # Clean the abstracts
    abstracts = [clean(text=abstract,
                      fix_unicode=True,
                      to_ascii=True,
                      lower=True,
                      no_line_breaks=False,
                      no_numbers=False,
                      no_punct=False,)
                 for abstract in abstracts]

    # Create a BERTopic model
    vectorizer_model = CountVectorizer(stop_words="english")
    topic_model = BERTopic(language="english", verbose=True, nr_topics=None, vectorizer_model=vectorizer_model)

    # If the old model exist, delete it
    if os.path.exists(savepath):
        os.remove(savepath)

    # Fit the model and save it
    topic_model.fit(abstracts)
    topic_model.save(savepath)
    print('Model saved!')

    # Print the time it took to train the model in hh:mm:ss format
    elapsed_time = time.time() - start_time
    print(time.strftime("Elapsed: %H:%M:%S", time.gmtime(elapsed_time)))

def main():
    # Load article abstracts
    print("Loading abstracts...")
    data = pd.read_csv("../../data/arxiv/arxiv.csv", dtype={"id": str, "abstract": str})

    print()

    # Train the tiny topic model
    print("Training tiny topic model...")
    train_topic_model(data, size=0.01, savepath="../../models/topic_model-tiny")

    # Train the small topic model
    print("Training small topic model...")
    train_topic_model(data, size=0.1, savepath="../../models/topic_model-small")

    # Train the medium topic model
    print("Training medium topic model...")
    train_topic_model(data, size=0.5, savepath="../../models/topic_model-medium")

    # Train the large topic model
    print("Training large topic model...")
    train_topic_model(data, size=1.0, savepath="../../models/topic_model-large")


if __name__ == "__main__":

    main()