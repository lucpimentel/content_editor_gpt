import streamlit as st
import openai
from auxfunctions import openai_api_call


openai.api_key = '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'

st.title('Welcome to the GPT Content Editor App!')


draft_paragraph = st.text_input('Please insert your draft paragraph:')


prompt = f'Please correct this draft paragraph: {draft_paragraph}'


button_isClicked = st.button("Correct Paragraph")


# Create a button to call the function
if button_isClicked:
    with st.spinner("Loading..."):
        response_text = openai_api_call(prompt)
        st.text_area('Corrected Paragraph:',response_text,height = 200)
        button_isClicked = False
