import streamlit as st

# Ocultar la barra superior, el pie de página y los botones flotantes inferiores
hide_st_style = """
    <style>
    /* Oculta la barra de herramientas superior */
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    /* Oculta los botones y elementos flotantes de la parte inferior derecha */
    [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    .stApp > footer {data-testid: hidden !important;}
    [data-testid="manage-app-button"] {visibility: hidden !important; display: none !important;}
    button[title="View app in Streamlit Community Cloud"] {visibility: hidden !important; display: none !important;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Tu código original
st.title("🚧 Aplicación bajo construcción 🚧")
st.subheader("Estamos trabajando en nuevas funciones.")

st.info("Esta aplicación se encuentra actualmente bajo desarrollo. ¡Vuelve pronto para ver las novedades!")