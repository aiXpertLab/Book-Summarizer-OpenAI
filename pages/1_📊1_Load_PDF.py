#   st.session_state['article_content'] = article_content

import streamlit as st
from utils.st_def import st_logo, st_load_book, st_sidebar

st_logo(title='Welcome 👋 to Book Summarizer!', page_title="PDF Summarizer",)
st_load_book()
st_sidebar()

pdf1 = st.file_uploader('Upload your PDF Document', type='pdf')
#-----------------------------------------------
import openai, PyPDF2, os, time, pandas as pd
if pdf1:
    pdfReader = PyPDF2.PdfReader(pdf1)
    if 'pdfreader' not in st.session_state:   st.session_state['pdfreader'] = pdfReader
    st.markdown(" has loaded.")
else:
    st.markdown("waiting for loading ...")