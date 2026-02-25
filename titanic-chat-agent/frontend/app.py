import streamlit as st
import requests
from PIL import Image

st.title("🚢 Titanic Smart Chat Agent")

question = st.text_input("Ask a question about Titanic dataset:")

if st.button("Ask"):
    response = requests.post(
        "https://your-backend-name.onrender.com/ask",
        json={"question": question}
    )

    data = response.json()

    if "text" in data:
        st.write(data["text"])

    if "image" in data:
        image = Image.open(data["image"])
        st.image(image)