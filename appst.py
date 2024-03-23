import streamlit as st
import customtkinter as ctk
from PIL import Image, ImageTk
from auth_token import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Initialize StableDiffusionPipeline
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.to(device)

# Define function to generate image
def generate_image(text_input):
    with autocast(device):
        image = pipe(text_input, guidance_scale=8.5)["sample"][0]
    return image


# Customizing Streamlit appearance
st.set_page_config(
    page_title="Diffuse-Art 🎨",
    page_icon="🖼️",
    layout="wide",
    
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Settings")
st.sidebar.image("https://static.javatpoint.com/definition/images/art-definition.png", width=200)  # Adjust width as needed
st.sidebar.subheader("Instructions")
st.sidebar.write("1. Enter your prompt in the text area.")
st.sidebar.write("2. Click the 'Generate' button to create an image.")
# Main content
st.title("Diffuse-Art 🎨")

# Text input for prompt
prompt = st.text_area("Enter Prompt:", height=10)

# Button to generate image
if st.button("Generate"):
    if prompt:
        # Function to generate image
        st.write("🎨 Generating artwork...")
        generated_image = generate_image(prompt)
        st.image(generated_image, caption="Generated Image", use_column_width=True)
        st.success("✨ Artwork generated successfully!")

# Fun comment
st.info("Pro tip: The right prompt can lead to magical creations! 🧙✨")


