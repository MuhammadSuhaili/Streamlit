import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Perbandingan Canny Edge Detection: Fixed vs Adaptive Threshold")

# Upload gambar
uploaded_file = st.file_uploader("📂 Upload gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Baca gambar dan konversi ke format OpenCV
    img = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(img)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Deteksi tepi dengan threshold tetap
    canny_fixed = cv2.Canny(img_gray, 100, 200)

    # Deteksi tepi dengan threshold adaptif berdasarkan median piksel
    median_val = np.median(img_gray)
    lower = int(max(0, 0.8 * median_val))
    upper = int(min(255, 1.2 * median_val))
    canny_adaptive = cv2.Canny(img_gray, lower, upper)

    # Tampilkan info threshold
    st.markdown(f"**Median nilai piksel grayscale**: `{median_val}`")
    st.markdown(f"**Threshold Adaptive Canny** → Lower: `{lower}`, Upper: `{upper}`")

    # Tampilkan hasil dalam 3 kolom
    st.subheader("📸 Hasil Deteksi Tepi")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(img, caption="Original", use_container_width=True)

    with col2:
        st.image(canny_fixed, caption="Canny Fixed", use_container_width=True, channels="GRAY")

    with col3:
        st.image(canny_adaptive, caption="Adaptive Canny", use_container_width=True, channels="GRAY")
