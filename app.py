import streamlit as st
from groq import Groq

st.set_page_config(page_title = 'AI Interview Assistant', layout='centered')
st.title('AI Interrview Assistant')
st.caption('Practice interviews  with AI-Generated questions and constructive feedback.')
st.caption('Launched by Preetam Rathod')
st.write('Department of AI DS')

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write('API connection successful')
except (KeyError, FileNotFoundError):
  st.error('Groq_API_KEY is missing. Add it to streamlit  cloud --> app setting')
  st.stop()
#creating dropdown for roles
role = st.selectbox("Select the Job Role",[
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Machine Learning Engineer",
  "Software Engineer",
  "HR Executive"
])
