import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Placeholder function – will be replaced by real model later
def generate_digit_images(digit: int, num_images: int = 5):
    images = []
    for _ in range(num_images):
        img = Image.new("L", (28, 28), color=0)
        images.append(np.array(img))
    return images

st.set_page_config(page_title="Digit Generator", layout="centered")
st.title("✍️ Handwritten Digit Image Generator")
st.markdown("Generate synthetic MNIST-like images using your trained model.")

digit = st.selectbox("Choose a digit to generate (0–9):", list(range(10)))

if st.button("Generate Images"):
    st.subheader(f"Generated images of digit {digit}")
    images = generate_digit_images(digit, num_images=5)

    cols = st.columns(5)
    for i, (col, img) in enumerate(zip(cols, images)):
        with col:
            st.image(img, width=100, caption=f"Sample {i+1}")
