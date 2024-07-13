import streamlit as st
import os
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
from duckduckgo_search import DDGS

def chat(self, keywords: str, model: str = "gpt-3.5", timeout: int = 20) -> str:
    """Initiates a chat session with DuckDuckGo AI.

    Args:
        keywords (str): The initial message or question to send to the AI.
        model (str): The model to use: "gpt-3.5", "claude-3-haiku", "llama-3-70b", "mixtral-8x7b".
            Defaults to "gpt-3.5".
        timeout (int): Timeout value for the HTTP client. Defaults to 20.

    Returns:
        str: The response from the AI.
    """

# Set the page title and layout
st.set_page_config(page_title="Home", layout="wide")
st.title("Home")


if "inspirasi" not in st.session_state:
    st.session_state["inspirasi"] = ""

if "lini bisnis" not in st.session_state:
    st.session_state["lini bisnis"] = ""

input=st.session_state["lini bisnis"]
st.subheader(f"Inspirasi bisnis Anda dalam lini {input}")

with st.sidebar:
    st.session_state["lini bisnis"] = st.text_input("Tuliskan lini bisnis Anda: ")
    cari = st.button("Cari", key="cari")

if cari and st.session_state["lini bisnis"] != "":
        st.session_state["inspirasi"] = DDGS().chat(f"Tuliskan hasil pencarian dalam bahasa indoensia yang jelas dan informatif.Analisa bisnis dalam lini {input} yang paling cocok dijalankan di Tahun 2024 dalam konteks bisnis Indonesia. Bisnis tersebut harus bisa dijalnkan oleh UMKM, buatkan juga alasan dari masing masing masukan tersebut. Tuliskan sumber bacaan dan link untuk masing masing usulan bisnis", model='llama-3-70b')
        

if "inspirasi" in st.session_state: 
     st.session_state["inspirasi"]
else:
     st.write("Silahkan tulis lini bisnis yang ingin Anda riset")

#st.session_state
        
    
