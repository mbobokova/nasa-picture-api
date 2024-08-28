import streamlit as st
import requests


# API Setting
api_key = "niAiTqXDqVk8xpfCTV5VClIKA7xj8lldAvoGl48z"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Request data
response = requests.get(url)
data = response.json()

# Get image, description and url
title = data["title"]
description = data["explanation"]
image_url = data["url"]

# Download the IMAGE
image_filepath = "images/image.png"
img_response = requests.get(image_url)

with open("images/image.png", "wb") as file:
    file.write(img_response.content)

# Front End
st.header(title)
st.write(description)
st.image(image_filepath)
