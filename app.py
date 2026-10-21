import streamlit as st

# Ocultar la barra de herramientas, menú y pie de página
hide_github_style = """
    <style>
    [data-testid="stToolbar"] {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_github_style, unsafe_allow_html=True)

# Tu código original
st.title("🚧 Aplicación bajo construcción 🚧")
st.subheader("Estamos trabajando en nuevas funciones.")

st.info("Esta aplicación se encuentra actualmente bajo desarrollo. ¡Vuelve pronto para ver las novedades!")