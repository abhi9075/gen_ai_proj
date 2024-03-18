# integrate with OpenAI
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ['OPENAI_API_KEY']= openai_key

# stremlit framework

st.title("Langchain With Open AI")
input_text = st.text_inpt("Search the topic")

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm(input_text))