# st.session_state['frequency_table'] = frequency_table
import streamlit as st, time
from utils import st_def, ut_openai

st_def.st_logo(title = "Welcome 👋 to Summary!", page_title="Summary",)
st_def.st_summary()
summary = ''
openai_api_key= st_def.st_sidebar()
#------------------------------------------------------------------------
if 'txtfrompdf' not in st.session_state:   
  st.info('Read PDF before continue ... ')
else:
  text = st.session_state['txtfrompdf']
  if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
  else: 
    for i in range(len(text)):
      prompt =f"""
        Your task is to extract relevant information from a text on the page of a book. This information will be used to create a book summary.
        Extract relevant information from the following text, which is delimited with triple backticks.\
        Be sure to preserve the important details.
        Text: ```{text[i]}```
      """
      stream = ut_openai.aichat(openai_api_key=openai_api_key, 
                                messages = [{"role": "user",   "content": prompt},])

      response = st.write(stream)
      summary = summary+' ' +stream.choices[0].message.content +'\n\n'
      time.sleep(19)  #You can query the model only 3 times in a minute for free, so we need to put some delay
      
    st.write(summary)