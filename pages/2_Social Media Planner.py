import streamlit as st
import os
from llama_index.llms.groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load Groq API key from environment
GROOQ_API_KEY = os.getenv("GROOQ_API_KEY")

# Initialize Groq LLM instance
llm = Groq(model="llama3-70b-8192", api_key=GROOQ_API_KEY)

def generate_content(prompt):
    response = llm.complete(prompt)
    return response

# Set page configuration
st.set_page_config(layout="wide", page_title="Business Plan")
st.title("Social Media Planner")
st.write("Disini anda bisa mendapatkan inspirasi konten untuk sosial media Anda")

# Initialize session state variables if not present
if "business_resume" not in st.session_state:
    st.session_state["business_resume"] = None
if "sosmed_plan" not in st.session_state:
    st.session_state["sosmed_plan"] = None
if "sosmedPlanDetail" not in st.session_state:
    st.session_state["sosmedPlanDetail"] = None

sosial_media_plan = st.session_state["sosmed_plan"]

# Sidebar content
with st.sidebar:
    st.title("Data Bisnis Anda")
    sosmed_plan = st.text_area(label="Tuliskan rencana konten Anda disini:", height=300)
    create_sosmed=st.button("Create Sosmed")

    if sosmed_plan != "" and create_sosmed:
        sosmedPlanDetailPrompt = f"Analisa {sosmed_plan}. Perhatikan sosial media rekomdenasi dari {sosmed_plan} dan buatkan rencana konten untuk masing - masing platform dalam format tabel dengan bahasa indonesia yang baik dan benar untuk 2 minggu dengan tayang 2 hari sekali. Format output adalah waktu tayang, prompt image, copywriting/caption, hashtag"
        st.session_state["sosmedPlanDetail"] = generate_content(sosmedPlanDetailPrompt)
        
    #if st.session_state["sosmed_plan"]=="":       
        #create_sosmed=st.button("Create Sosmed")

    
    
st.markdown(f'<div class="stock-analysis">{st.session_state["sosmedPlanDetail"]}</div>', unsafe_allow_html=True)
        

    #else:
        #resumeSosmedPlanPrompt=f"Buatlah ringkasan dari {sosial_media_plan} dengan hanya menampillkan rekomendasi sosial meda platform dan sosial media strategy"
        #resumeSosmedPlan = generate_content(resumeSosmedPlanPrompt)
        #st.text_area(label="Tuliskan rencana konten Anda disini:", height=200, value=resumeSosmedPlan)
        #st.markdown(f'<div class="stock-analysis">{resumeSosmedPlan}</div>', unsafe_allow_html=True)   
        #st.text_area(textResume, height=400)

# Main page content

# Memastikan st.session_state["sosmedPlanDetail"] hanya dijalankan jika sosmedPlanDetail kosong dan st.session_state["sosmed_plan"] berisi data
if st.session_state["sosmedPlanDetail"] is None and st.session_state["sosmed_plan"] is not None:
    sosmedPlanDetailPrompt = f"Analisa {sosial_media_plan}. Perhatikan sosial media rekomdenasi dari {sosial_media_plan} dan buatkan rencana konten untuk masing - masing platform dalam format tabel dengan bahasa indonesia yang baik dan benar untuk 2 minggu dengan tayang 2 hari sekali. Format output adalah waktu tayang, prompt image, copywriting/caption, hashtag"
    st.session_state["sosmedPlanDetail"] = generate_content(sosmedPlanDetailPrompt)

# Menampilkan hasil jika st.session_state["sosmed_plan"] berisi data
if st.session_state.get("sosmed_plan") is not None:
    st.markdown(f'<div class="stock-analysis">{st.session_state["sosmedPlanDetail"]}</div>', unsafe_allow_html=True)
else:
    st.write("")

