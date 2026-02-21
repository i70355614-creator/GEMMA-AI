import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyD73YtOUSL_Zp_5fm1aI83rzy-8jo0KnKo")

st.title("GEMMA AI")

intrebare = st.chat_input("Scrie ceva aici....")

if intrebare:

    model=genai.GenerativeModel("gemini-pro")
    try:
        response = model.generate_content(intrebare)
        st.write(response.text)
    except Exception as e:

        st.error(f"A aparut o problema: {e}")



