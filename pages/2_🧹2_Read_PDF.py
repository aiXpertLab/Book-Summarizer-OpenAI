import streamlit as st
from utils.st_def import st_logo, st_read_pdf

st_logo(title = "Welcome 👋 to Text Cleaning!", page_title="Text Cleaning",)
st_read_pdf()
#------------------------------------------------------------------------
import openai, PyPDF2, os, time, pandas as pd

# pdfReader = PyPDF2.PdfReader(st.session_state['pdf'])
text=[]
summary=' '
pr = st.session_state['pdfreader']
with st.spinner('Loading files...'):
  #Storing the pages in a list
  for i in range(0,len(pr.pages)):
    # creating a page object
    pageObj = pr.pages[i].extract_text()
    pageObj= pageObj.replace('\t\r','')
    pageObj= pageObj.replace('\xa0','')
    # extracting text from page
    text.append(pageObj)
    
if 'txt' not in st.session_state:   st.session_state['txt'] = text
st.write(text)