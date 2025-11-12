import streamlit as st

st.set_page_config(page_title="Futuristic Health AI", layout="centered")

st.markdown("""
    <style>
    body {
        background: radial-gradient(circle at 20% 30%, #0b0c10, #1f2833, #0b0c10);
        background-attachment: fixed;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.pinimg.com/originals/8a/58/4c/8a584c5b93f60cb329a4c25b36cf1d36.gif");
        background-size: cover;
        background-attachment: fixed;
    }
    h1 {
        text-align: center;
        color: #66fcf1;
        text-shadow: 0 0 20px #ff073a;
    }
    .main-btn {
        background: linear-gradient(90deg, #ff073a, #045de9);
        color: white;
        font-weight: bold;
        font-size: 20px;
        border: none;
        padding: 15px 30px;
        border-radius: 15px;
        box-shadow: 0 0 25px #045de9;
        transition: all 0.3s ease-in-out;
    }
    .main-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 0 35px #ff073a;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🌌 Futuristic Health AI Portal</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; font-size:18px; color:#c5c6c7;'>
Welcome to the next generation of <b>AI-driven health intelligence</b>.  
Explore personalized risk predictions, scientific insights, and preventive health guidance — all powered by machine learning.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("🚀 Start Diabetes Risk Prediction", use_container_width=True):
   st.switch_page("pages/2_Diabetes_Predictor.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#45a29e;'>© 2025 Futuristic Health AI | Designed with ❤️ using Streamlit</div>", unsafe_allow_html=True)
