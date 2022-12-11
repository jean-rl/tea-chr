import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os

st.set_page_config(layout="centered", page_icon="☕", page_title="Tea-chr", initial_sidebar_state="collapsed", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
st.title("☕ Tea-chr")
st.header("A tool that helps you build background before reading a scientific paper 📑")

st.markdown("Are you about to start reading a paper about a new topic? This tool is perfect for begginer researchers that want to have the background before jumping to the full topic")

st.image("data/sample_image.png", caption="Overview of our tool in work")

#st.markdown("Get the topics ready before reading!")
st.info('Get the topics ready before reading!', icon="ℹ️")
#st.header("Load your paper to start!")

for (root,dirs,files) in os.walk(os.getcwd(), topdown=True):
    st.write(root, dirs, files)

left, mid, right = st.columns([1,1,1])
#col2.title("Centered! :)") 

with mid:
    st.subheader("Try it out now")
    file = st.file_uploader(label="Choose file", type="pdf", label_visibility="hidden")
    if file != None:
        bytes_data = file.getvalue()
        with open("file.pdf", "wb") as writer:
            writer.write(bytes_data)
        #bytes_data = file.getvalue()
        #st.write(bytes_data)
    #st.session_state['file'] = bytes_data # Dictionary like API

if file != None:
    switch_page("teachr")
