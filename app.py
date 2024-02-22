import streamlit as st
import textwrap
import PIL.Image
# from IPython.display import Markdown
from IPython.display import display
from IPython.display import Markdown
# from PIL import Image


import google.generativeai as genai

# Configure the Google API key
genai.configure(api_key='AIzaSyCWhUYwDc_QwEneu_f9Z5NgNunNY943_cA')



# Function to generate text from text input
def generate_text(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def generate_text_from_image(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["Write a short, engaging blog post based on this picture",image],stream=True)
    response.resolve()
    return response.text

# Streamlit app
def main():
    st.title("Gemini Pro Text-Text and Image-Text Generator")

    input_type = st.radio("Select input type:", ("Text", "Image"))

    if input_type == "Text":
        input_text = st.text_area("Enter text:")
        if st.button("Generate"):
            if input_text:
                generated_text = generate_text(input_text)
                st.markdown(generated_text)
            else:
                st.warning("Please enter some text.")

    elif input_type == "Image":
        image_file = st.file_uploader("Upload an image:")
        if image_file is not None:
            image = PIL.Image.open(image_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            if st.button("Generate"):
                generated_text = generate_text_from_image(image)
                st.markdown(generated_text)

if __name__ == "__main__":
    main()

