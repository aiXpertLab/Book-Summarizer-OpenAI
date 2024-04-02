# st.session_state['frequency_table'] = frequency_table
import streamlit as st
from utils.st_def import st_logo, st_text_cleaning_contents

st_logo(title = "Welcome 👋 to Summary!", page_title="Summary",)
st_text_cleaning_contents()

#------------------------------------------------------------------------
text = st.session_state('txt')
for i in range(len(text)):
  prompt =f"""
  Your task is to extract relevant information from a text on the page of a book. This information will be used to create a book summary.
  Extract relevant information from the following text, which is delimited with triple backticks.\
  Be sure to preserve the important details.
  Text: ```{text[i]}```
  """
  try:
    response = get_completion(prompt)
  except:
    response = get_completion(prompt)
  print(response)
  summary= summary+' ' +response +'\n\n'
  result.append(response)
  time.sleep(19)  #You can query the model only 3 times in a minute for free, so we need to put some delay