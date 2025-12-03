import streamlit as st
import cv2
import numpy as np
from Scripts.utils import load_image, to_streamlit_image
from Scripts.qr_scanner import decode_qr
from Scripts.doc_scanner import scan_document

st.set_page_config(page_title="Quick Actions", page_icon="⚡", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

st.markdown('<div class="hero-container"><div class="hero-title">Quick Actions</div></div>', unsafe_allow_html=True)

# Tabs for different tools
tab1, tab2, tab3 = st.tabs(["📷 QR Scanner", "📄 Doc Scanner", "📸 Camera Capture"])

# --- QR SCANNER ---
with tab1:
    st.markdown("### 🔍 Scan QR Code")
    st.write("Upload an image or take a photo to scan a QR code.")
    
    img_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'], key="qr_upload")
    camera_img = st.camera_input("Take a Photo", key="qr_cam")
    
    input_img = img_file if img_file else camera_img
    
    if input_img:
        # Process
        img_array = load_image(input_img)
        data, result_img = decode_qr(img_array)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(input_img, caption="Original Image", use_container_width=True)
        with col2:
            st.image(to_streamlit_image(result_img), caption="Processed Image", use_container_width=True)
            
        if data:
            st.success(f"**QR Code Detected:** {data}")
        else:
            st.warning("No QR code detected.")

# --- DOC SCANNER ---
with tab2:
    st.markdown("### 📄 Document Scanner")
    st.write("Auto-detects document edges and creates a scanned PDF-like view.")
    
    img_file_doc = st.file_uploader("Upload Document Image", type=['jpg', 'png', 'jpeg'], key="doc_upload")
    camera_img_doc = st.camera_input("Take a Photo", key="doc_cam")
    
    input_img_doc = img_file_doc if img_file_doc else camera_img_doc
    
    if input_img_doc:
        img_array = load_image(input_img_doc)
        scanned, debug_img = scan_document(img_array)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(to_streamlit_image(debug_img), caption="Detected Edges", use_container_width=True)
        with col2:
            st.image(to_streamlit_image(scanned), caption="Scanned Result", use_container_width=True)

# --- CAMERA CAPTURE ---
with tab3:
    st.markdown("### 📸 Simple Capture")
    st.write("Just a simple camera capture tool.")
    
    cam_pic = st.camera_input("Take a Picture", key="simple_cam")
    
    if cam_pic:
        st.image(cam_pic, caption="Captured Image", use_container_width=True)
        st.download_button("Download Image", cam_pic, "capture.jpg", "image/jpeg")
