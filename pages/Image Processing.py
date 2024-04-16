import os
import streamlit as st
from PIL import Image

# To set page
st.set_page_config(page_title="Image Processing", layout="centered", page_icon="🖼️")

st.title("🖼️ Image Processing")

working_dir = os.path.dirname(os.path.abspath(__file__))

images_dir = os.path.join(working_dir, "images")

image_names = [img_name for img_name in os.listdir(images_dir) if img_name.endswith((".jpg", ".jpeg", ".png"))]

# Load 
images = [Image.open(os.path.join(images_dir, img_name)) for img_name in image_names]

selected_image = st.selectbox("Select an image", image_names)

# Display
st.subheader("Original Image")
st.image(images[image_names.index(selected_image)])



# Image processing o
resize_option = st.checkbox("Resize")
grayscale_option = st.checkbox("Grayscale Conversion")
crop_option = st.checkbox("Image Cropping")
rotate_option = st.checkbox("Image Rotation")


processed_image = images[image_names.index(selected_image)].copy()

if resize_option:
    width = st.slider("Select width for resizing", min_value=50, max_value=1000, value=300)
    height = st.slider("Select height for resizing", min_value=50, max_value=1000, value=300)
    processed_image = processed_image.resize((width, height))

if grayscale_option:
    processed_image = processed_image.convert("L")

if crop_option:
    left = st.slider("Select left coordinate for cropping", min_value=0, max_value=processed_image.width - 1, value=0)
    top = st.slider("Select top coordinate for cropping", min_value=0, max_value=processed_image.height - 1, value=0)
    right = st.slider("Select right coordinate for cropping", min_value=left + 1, max_value=processed_image.width, value=processed_image.width)
    bottom = st.slider("Select bottom coordinate for cropping", min_value=top + 1, max_value=processed_image.height, value=processed_image.height)
    processed_image = processed_image.crop((left, top, right, bottom))

if rotate_option:
    angle = st.slider("Select angle for rotation", min_value=0, max_value=360, value=0)
    processed_image = processed_image.rotate(angle)

# Display image
if any([resize_option, grayscale_option, crop_option, rotate_option]):
    st.subheader("Processed Image")
    st.image(processed_image)


