import streamlit as st
import urllib
import base64

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
st.title("👨‍💼 Tea-chr - a tool to give you background before reading a paper")

left, right = st.columns([3,1], gap="small")

with left:
    st.header("Aquí va el paper cargado")
    show_pdf("file.pdf")

with right:
    st.header("Aquí irán los conceptos y sus explicaciones")
    pass
#displayPDF("https://arxiv.org/pdf/1706.03762.pdf")