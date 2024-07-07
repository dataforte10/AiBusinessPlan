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

# Page configuration
st.set_page_config(page_title="Business Assistant", layout="wide")

#st.header("Business Assistant")
# Sidebar
with st.sidebar:
    st.header("Business Assistant")
    st.write("Rekan Anda dalam membuat dan merancang bisnis plan.")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Ide Bisnis", "Deskripsi Bisnis", "Rencana Bisnis", "Sosial media"])

# Session cache for storing form data
if 'business_idea' not in st.session_state:
    st.session_state['business_idea'] = {
        'what': '',
        'why': '',
        'where': '',
        'when': '',
        'who': '',
        'how': ''
    }

def update_business_idea():
    st.session_state.business_idea['what'] = what_data
    st.session_state.business_idea['why'] = why_data
    st.session_state.business_idea['where'] = where_data
    st.session_state.business_idea['when'] = when_data
    st.session_state.business_idea['who'] = who_data
    st.session_state.business_idea['how'] = how_data

def clear_business_idea():
    st.session_state.business_idea = {
        'what': '',
        'why': '',
        'where': '',
        'when': '',
        'who': '',
        'how': ''
    }

def generate_content(prompt):
    response = llm.complete(prompt)
    return response

def raw_data(what_data, why_data, where_data, when_data, who_data, how_data):
    """
    Generates a business data template with provided information.

    Parameters:
    what_data (str): Description of the business idea.
    why_data (str): Background or reason for creating the business.
    where_data (str): Location where the business will be implemented.
    when_data (str): Timing or moment to start the business.
    who_data (str): Target audience or customers for the business.
    how_data (str): Plan or strategy for running the business.

    Returns:
    str: A formatted string containing the business data.
    """
    template = (
        f"Ini adalah data bisnis yang akan dibuat. Bisnis ini adalah {what_data}. "
        f"Latar belakang saya membuat bisnis ini adalah {why_data}. "
        f"Bisnis ini akan diterapkan di {where_data}. "
        f"Waktu menjalankan bisnis ini adalah {when_data}. "
        f"Target bisnis ini adalah {who_data}. "
        f"Rencana bisnis ini adalah sebagai berikut: {how_data}."
        f"berdasarkan data tersebut, tuliskan rencana bisnis yang sesuai dengan data tersebut. Tuliskan dalam bentuk narasi yang jelas dan infomarmatif dalam bahasa indonesia"
        f"struktur tulisan dengan membuat bisnis model canvas"
    )
    return template

def generate_business_plan():
    # Generate the business data template
    result = raw_data(
        what_data=st.session_state.business_idea['what'],
        why_data=st.session_state.business_idea['why'],
        where_data=st.session_state.business_idea['where'],
        when_data=st.session_state.business_idea['when'],
        who_data=st.session_state.business_idea['who'],
        how_data=st.session_state.business_idea['how']
    )    

    # Run the LLM with the generated prompt
    business_plan = generate_content(result)
    return business_plan

with tab1:
    st.header("Ide Bisnis")
    st.write("Gambarkan ide bisnis Anda, sebagai panduan,silahkan tuliskan 5W 1H dari ide bisnis Anda.")

    what_data = st.text_area(
        label="Apa ide bisnis anda",
        help="Gambarkan secara garis besar ide bisnis anda",
        placeholder="Gambarkan ide bisnis anda",
        height=100,
        value=st.session_state.business_idea['what']
    )

    why_data = st.text_input(
        label="Apa yang melatar belakangi ide bisnis anda",
        help="Gambarkan secara garis besar ide bisnis anda",
        placeholder="Gambarkan ide bisnis anda",
        value=st.session_state.business_idea['why']
    )

    col1, col2 = st.columns(2)

    with col1:
        where_data = st.text_input(
            label="Dimana sebaiknnya ide bisnis ini diterapkan",
            help="Misal online, offline, ruko, rumahan dsb",
            placeholder="Gambarkan ide bisnis anda",
            value=st.session_state.business_idea['where']
        )

    with col2:
        when_data = st.text_input(
            label="Kapan bisnis anda punya momentum",
            help="Business momentum",
            placeholder="Gambarkan ide bisnis anda",
            value=st.session_state.business_idea['when']
        )

    who_data = st.text_input(
        label="Siapa target pasar anda?",
        help="Gambarkan secara garis besar ide bisnis anda",
        placeholder="Gambarkan ide bisnis anda",
        value=st.session_state.business_idea['who']
    )

    how_data = st.text_area(
        label="Bagaimana bisnis anda berjalan?",
        help="Secara online, melalui offline, ruko, rumahan dsb",
        placeholder="Gambarkan ide bisnis anda",
        height=200,
        value=st.session_state.business_idea['how']
    )

    create_button, reset_button = st.columns(2)
    with create_button:
        if st.button(
            label="Create business plan",
            type="primary"
        ):
            update_business_idea()
            st.success("Business idea updated successfully!")
    with reset_button:
        if st.button(
            label="Reset",
            type="secondary"
        ):
            clear_business_idea()
            st.success("Cleared Form")

if st.session_state['business_idea']['what']:
    with tab2:
        with st.spinner("Generating business plan..."):
            st.subheader("Business Plan")
            business_plan = generate_business_plan()
            st.write(business_plan)

    with tab3:
        with st.spinner("Generation Rencana eksekusi"):
            st.subheader("Rencana aksi (action plan)")
            prompt_eksekusi=f"Buat dalam bahasa Indoensia yang informatif,Berdasarkan {business_plan} yang sudah dibuat,buatkan rencana pelaksanaan bisnis dengan alur sebagai berikut:1.hal pertama yang harus dikerjakan[bila dirasa perlu membuat badan hukum, buatlah badan hukum dengan menggunakan SSO]\n"
            plan_eksekusi = generate_content(prompt_eksekusi)
            st.markdown(f'<div class="stock-analysis">{plan_eksekusi}</div>', unsafe_allow_html=True)

    with tab4:
        with st.spinner("Generate sosial media strategy"):
            st.subheader("Sosial media yang diusulkan")
            prompt_sosmed= f"Buat dalam bahasa Indoensia yang informatif,berdasarkan {business_plan} yang sudah dibuat,buatkan rencana sosial media yang harus dikerjakan dalam bisnis.Tampilkan rekomendasi sosial media apa yang paling sesuai untuk industri dan bisnis yang ditulis dan sertakan alasan dari pemilihan sosial media tersebut."
            sosmed_plan = generate_content(prompt_sosmed)
            st.markdown(f'<div class="stock-analysis">{sosmed_plan}</div>', unsafe_allow_html=True)
            st.subheader("Usulan konten sosial media")
            prompt_konten= f"berdasarkan pilihan sosial media {sosmed_plan} yang sudah dibuat, buatkan usulan konten dengan struktur: jenis sosial media, usul konten(kalau gambar tuliskan prompt, atau script untuk video), dan copywriting yang sesuai dengan konten yang ada "
            konten_plan = generate_content(prompt_konten)
            st.markdown(f'<div class="stock-analysis">{konten_plan}</div>', unsafe_allow_html=True)

    prompt_draft=f"Buat dalam bahasa Indoensia yang informatif berdasarkan {business_plan} yang sudah dibuat, hanya buatkan ringkasan berupa poin poin dari bisnis inside dengan data : Jenis bisnis (Jasa, FMCG, Retail, Perdagangan, lainnya), target pasar, peraturan pemerintah apa yang harus ditaati. tidak perlu menampilkan key point "
    business_draft=generate_content(prompt_draft)
    business_resume=st.sidebar.markdown(f'<div class="stock-analysis">{business_draft}</div>', unsafe_allow_html=True)

            
