import streamlit as st


def get_question():

    return st.chat_input(
        "Ask about an aviation investigation..."
    )
