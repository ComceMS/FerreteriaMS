import streamlit as st

# Ocultar barra superior, menú, pie de página y widgets flotantes de perfil/Streamlit
hide_st_style = """
    <style>
    /* Oculta la barra superior (menú, toolbar y botón de GitHub/Fork) */
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    /* Oculta los iconos y tarjetas flotantes de la esquina inferior derecha */
    [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    [data-testid="manage-app-button"] {visibility: hidden !important; display: none !important;}
    div[class*="stAppBadge"] {visibility: hidden !important; display: none !important;}
    div[data-baseweb="popover"] {visibility: hidden !important; display: none !important;}
    iframe[title="streamlit_app"] {display: none !important;}
    
    /* Oculta cualquier contenedor relativo al perfil en la esquina inferior */
    .stApp > div:last-child {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Tu código
st.title("🚧 Aplicación bajo construcción 🚧")
st.subheader("Estamos trabajando en nuevas funciones.")

st.info("Esta aplicación se encuentra actualmente bajo desarrollo. ¡Vuelve pronto para ver las novedades!")