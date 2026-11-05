import streamlit as st
import base64

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Dano Tattuu", page_icon="logo.png", layout="centered")

# --- CSS PERSONALIZADO (Estilo Oscuro con Tarjeta Blanca para el Logo) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E0E0E; }
    h1, h2, h3, p, div { color: #FFFFFF !important; text-align: center; font-family: 'Helvetica'; }
    
    /* TRUCO: Recuadro blanco para el logo */
    .logo-container {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px; /* Bordes redondeados */
        width: 250px;
        margin: 0 auto; /* Centrar */
        margin-bottom: 20px;
        display: flex;
        justify-content: center;
        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.1);
    }

    /* Estilo para los botones de PDF */
    .link-container {
        background-color: #1A1A1A;
        border: 1px solid #FFFFFF;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    .link-container a {
        color: #FFFFFF !important;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
    }
    .link-container a:hover { color: #B22222 !important; }
    
    /* Caja para el botón de Google Reviews */
    .review-box {
        background-color: #B22222;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(178, 34, 34, 0.4);
    }
    .review-link {
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

def crear_enlace_pdf(archivo, texto):
    try:
        with open(archivo, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        href = f'<div class="link-container"><a href="data:application/pdf;base64,{base64_pdf}" target="_blank">{texto}</a></div>'
        st.markdown(href, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"⚠️ Falta el archivo {archivo}. Ejecuta crear_pdf.py")

# --- INTERFAZ VISUAL ---
# Convertir la imagen a base64 para meterla dentro de nuestro recuadro HTML
try:
    with open("logo.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    # Mostramos el HTML con la tarjeta blanca y la imagen adentro
    st.markdown(f'''
        <div class="logo-container">
            <img src="data:image/png;base64,{encoded_string}" width="200">
        </div>
    ''', unsafe_allow_html=True)
except:
    st.warning("⚠️ Falta la imagen logo.png en la carpeta.")

st.title("DANO TATTUU")
st.write("Bienvenido a tu espacio de preparación y cuidados.")
st.write("---")

# Sección 1: Antes de la cita
st.subheader("📋 Antes de tu Cita")
st.write("Lee estas recomendaciones para que tu sesión sea perfecta.")
crear_enlace_pdf("Recomendaciones_Pre_Tatuaje.pdf", "👁️ Ver Recomendaciones PRE-Tatuaje")

st.write("") 

# Sección 2: Después de la cita
st.subheader("🧴 Después de tu Cita")
st.write("Sigue estos pasos para que tu tatuaje cicatrice perfectamente.")
crear_enlace_pdf("Cuidados_Post_Tatuaje.pdf", "👁️ Ver Cuidados POST-Tatuaje")

st.write("---")

# Sección 3: Reseña de Google
st.subheader("⭐ ¡Déjanos tu Reseña!")
st.write("Tu opinión es muy importante para nosotros.")

url_google = "https://g.page/r/Cf0jNF2uhmhEEBM/review"

st.markdown(f"""
    <div class="review-box">
        <a class="review-link" href="{url_google}" target="_blank">
            👉 HAZ CLIC AQUÍ PARA DEJAR TU COMENTARIO 👈
        </a>
    </div>
""", unsafe_allow_html=True)

# QR al final
st.write("")
st.write("O escanea este código con tu celular:")
try:
    # También le ponemos un mini recuadro blanco al QR para que resalte
    with open("QR_DanoTattuu.png", "rb") as qr_file:
        encoded_qr = base64.b64encode(qr_file.read()).decode()
    
    st.markdown(f'''
        <div class="logo-container" style="width: 220px; padding: 10px;">
            <img src="data:image/png;base64,{encoded_qr}" width="200">
        </div>
    ''', unsafe_allow_html=True)
except:
    pass