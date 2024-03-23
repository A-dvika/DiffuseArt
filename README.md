# Diffuse-Art 🎨

Welcome to Diffuse-Art, an innovative image generation application powered by Stable Diffusion, an open-source state-of-the-art (SOTA) model for text-to-image generation from Stability AI. In this project, we focus on utilizing the Stable Diff model through Hugging Face Diffusers and building an intuitive application using both Tkinter and Streamlit desktop with NVIDIA RTX 3050 4GB GPU support.

https://github.com/A-dvika/DiffuseArt/assets/115079077/e9ef48ab-a986-4a17-b24a-cf44ab8ea49c



## Features

✨ Generate captivating digital artworks using Stable Diffusion algorithms  
✨ User-friendly interface powered by Tkinter and Streamlit  
✨ GPU acceleration for faster image processing  
✨ Seamless integration with Hugging Face Diffusers  
✨ Supports both text-based and interactive image generation  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Diffuse-Art.git
   ```

2. Install CUDA-enabled version of PyTorch:
   ```bash
   pip install torch==1.10.0+cuXXX torchvision==0.11.1+cuXXX torchaudio==0.10.0+cuXXX -f https://download.pytorch.org/whl/cuXXX/torch_stable.html
   ```
   (Replace `XXX` with your appropriate CUDA version)

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Hugging Face API token in `auth_token.py`:
   ```python
   HUGGINGFACE_API_TOKEN = "your_api_token_here"
   ```

## Usage

### Tkinter Application

Run the Tkinter-based application:
```bash
python app.py
```

### Streamlit Application

Run the Streamlit-based application:
```bash
streamlit run appst.py
```

