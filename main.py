from tkinter import Label
import langchain_helper as lch
import streamlit as st
import textwrap

st.title("Simple Internet Browser")

with st.sidebar:
    with st.form(key='my_form'):

        query = st.sidebar.text_area(
            label="Ask Wikipedia",
            max_chars=50,
            key="query"
        ),
        openai_api_key = st.text_input(
            label="Enter your OpenAI API key",
            type="password"
        ),

        submit_button = st.form_submit_button(label='Submit')

if query and openai_api_key:
    response = lch.langchain_agent(query, openai_api_key)
    st.text(textwrap.fill(response, width=80))
else:
    st.warning("Please enter a query and/or your OpenAI API key")