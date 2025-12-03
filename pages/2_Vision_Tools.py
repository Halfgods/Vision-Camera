import streamlit as st

st.set_page_config(page_title="Vision Tools", page_icon="👁️", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

st.markdown('<div class="hero-container"><div class="hero-title">Vision Tools</div></div>', unsafe_allow_html=True)

st.write("Placeholder for Vision Tools (Brightness, Contour, etc.)")
