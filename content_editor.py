import streamlit as st
import os
from langchain import LLMChain
from auxfunctions import chat_prompt
from langchain.chat_models import ChatOpenAI


st.title('Welcome to the GPT Content Editor App!')


api_key = st.text_input('What is your OpenAI API key?')

os.environ['OPENAI_API_KEY'] = api_key


draft_paragraph = st.text_input('Please insert your draft paragraph:')

try:
    llm = ChatOpenAI(model = 'gpt-4-0613', temperature = 0)

    llm_chain = LLMChain(llm = llm, prompt = chat_prompt)
except:
    pass

button_isClicked = st.button("Correct Paragraph")


# Create a button to call the function
if button_isClicked:
    with st.spinner("Loading..."):
        response_text = llm_chain.run(draft_paragraph)
        st.text_area('Corrected Paragraph:',response_text,height = 200)
        button_isClicked = False
