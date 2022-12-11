import sys
sys.path.append("..") # Adds higher directory to python modules path.

import streamlit as st
import urllib
import base64
from streamlit_extras.switch_page_button import switch_page
from generate_response import *
from extractdata import extract_text_from_pdf
from bertopic import BERTopic
import os

#function to display the PDF of a given file 
def displayPDF(file):
    # Opening file from file path. this is used to open the file from a website rather than local
    with urllib.request.urlopen(file) as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


st.set_page_config(layout="wide", page_icon="👨‍💼", page_title="Tea-chr", initial_sidebar_state="collapsed")
if st.button(label="Home"):
    switch_page("main_page")
st.title("☕ Tea-chr")
st.markdown("## A tool that gives you the *big picture* before diving into what is **important**")
st.markdown("-----------------------------------")

left, right = st.columns([3,2])
# left, right = st.columns([3,1]) Try this if you need more space for PDF displaying

st.info('Note: For now only Firefox browser renders the PDF without warning. Plase use it for full demonstration purposes.', icon="ℹ️")

with left:
    st.header("Your paper")
    st.markdown("Read the paper in this page")
    #st.markdown("""<embed src="https://drive.google.com/viewerng/viewer?embedded=true&url=https://arxiv.org/pdf/2212.04485.pdf" width="700" height="950">""", unsafe_allow_html=True)
    show_pdf("file.pdf")

text = extract_text_from_pdf("file.pdf")
# st.write(os.getcwd())
topic_model = BERTopic.load("/app/tea-chr/models/topic_model-tiny")
topics, _ = topic_model.transform(text)

for topic in set(topics):
    topics_text = [t[0] for t in topic_model.get_topic(topic)]

with right:
    # st.header("Aquí irán los conceptos y sus explicaciones")
    st.header("The main topics")
    st.markdown("Take a look at the most important topics before diving into the paper or alongside it...")
    number = st.number_input('Number of topics to generate', min_value=3, max_value=10, step=1)
    #subheader = '<p style="font-family:helvetica, sans-serif; color:orange; font-size: 28px;">reward</p>'
    #st.markdown(subheader, unsafe_allow_html=True)
    
    for i in range(number):
        st.subheader(topics_text[i])
        response = generate_responses(topics_text[i])
        st.caption(response)

left2, mid, right2 = st.columns([1,1,1])

#with mid:
#    st.header("Missing a topic?")
#    st.subheader("Write it down and get a response")
    
#displayPDF("https://arxiv.org/pdf/1706.03762.pdf")