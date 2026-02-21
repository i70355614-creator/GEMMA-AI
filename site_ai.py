import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBv3TMYQu1jICVVfn11zsbUKdVLqeGGLUM")

st.title("GEMMA AI")

intrebare = st.chat_input("Scrie ceva aici....")

if intrebare:

    model=genai.GenerativeModel("models/gemini-1.5-flash")
    try:
        response = model.generate_content(intrebare)
        st.write(response.text)
    except Exception as e:

        st.error(f"A aparut o problema: {e}")
