import streamlit as st
import base64

# Page Config
st.set_page_config(
    page_title="Vision Toolkit",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# Hero Banner
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Vision Toolkit</div>
        <div class="hero-subtitle">YOUR CAMERA, UPGRADED BY AI.</div>
    </div>
""", unsafe_allow_html=True)

# Helper function to create a clickable card
def card(icon, title, description, url):
    st.markdown(f"""
        <a href="{url}" class="card-link" target="_self">
            <div class="card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-desc">{description}</div>
            </div>
        </a>
    """, unsafe_allow_html=True)

# Section 1: Quick Actions
st.markdown('<div class="section-header"><h2>⚡ Quick Actions</h2></div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    card("📷", "Scan QR", "Instant QR code reader", "Quick_Actions")
with col2:
    card("📄", "Scan Doc", "Digitize documents fast", "Quick_Actions")
with col3:
    card("📸", "Capture", "High-res photo capture", "Quick_Actions")
with col4:
    card("✂️", "Crop", "Smart auto-cropping", "Vision_Tools")

# Section 2: Vision Tools
st.markdown('<div class="section-header"><h2>👁️ Vision Tools</h2></div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    card("🔆", "Brightness", "Low-light enhancement", "Vision_Tools")
with col2:
    card("🔪", "Contour", "Extract objects via contours", "Vision_Tools")
with col3:
    card("🎨", "Draw", "Virtual drawing on feed", "Vision_Tools")
with col4:
    card("📏", "Measure", "AR measurement tool", "Vision_Tools")

# Section 3: AI & AR Tools
st.markdown('<div class="section-header"><h2>🤖 AI / AR Tools</h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    card("🖼️", "Bg Cut", "Remove backgrounds instantly", "AI_AR_Tools")
with col2:
    card("🎯", "Track", "Real-time object tracking", "AI_AR_Tools")
with col3:
    card("📦", "AR Marker", "Detect ArUco markers", "AI_AR_Tools")

# Footer / Spacing
st.markdown("<br><br>", unsafe_allow_html=True)
