import streamlit as st
import os
from llama_index.llms.groq import Groq
from dotenv import load_dotenv

# Set the page title and layout
st.set_page_config(page_title="Home", layout="wide")
st.title("Home")


