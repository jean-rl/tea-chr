import os

from extractdata import extract_text_from_pdf
from bertopic import BERTopic

# Force pytorch to use CPU
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

def main():
    pdf_path = "../data/sample4.pdf"
    text = extract_text_from_pdf(pdf_path)

    topic_model = BERTopic.load("../models/topic_model-tiny")
    topics, _ = topic_model.transform(text)

    for topic in set(topics):
        print(topic, topic_model.get_topic(topic))

if __name__ == "__main__":
    main()