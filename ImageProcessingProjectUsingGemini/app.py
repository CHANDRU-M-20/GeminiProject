import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import langchain
import google.generativeai as genai
from template import prompt

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

multimodal = genai.GenerativeModel(model_name="gemini-pro-vision")

from PIL import Image

def get_byte_data(upload_images):
    if upload_images is not None:
        bytes_data = upload_images.getvalue()
        image_parts = [
            {
                'mime_type' : upload_images.type,
                'data':bytes_data

            }
        ]
        return image_parts
    
def get_response(prompt,byte_data,user_input):
    content = [prompt,byte_data[0],user_input]
    response = multimodal.generate_content(contents=content)
    return response


st.header("QA System")
upload_images = st.file_uploader("Upload the PNG or JPG File",type=['PNG','JPNG'])

user_input = st.text_input("Enter the query: ")
with st.expander('Check the Details'):
    st.write('Hello/.....')

if st.button('Submit'):
    if upload_images is not None:
        st.image(image=upload_images)
        if user_input and upload_images:
            byte_data = get_byte_data(upload_images)
            response = get_response(prompt,byte_data,user_input)
            if response:
                st.write(response.text)

if st.button('Reset'):
    st.session_state.clear()





