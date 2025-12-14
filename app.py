import streamlit as st
import joblib
import numpy as np
import pandas as pd 
from babel.numbers import format_currency

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------
try:
    with open('models/best_laptop_price_model.pkl', 'rb') as f:
        pipe = joblib.load(f)
except FileNotFoundError:
    st.error("Error: 'best_laptop_price_model.pkl' file not found.")
    st.stop()
except Exception as e:
    st.error(f"Error loading pipeline: {e}")
    st.stop()
    
st.markdown("<h1 style='text-align: center;'>Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------------
# 1. User Inputs
# ----------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    # Company
    company = st.selectbox('Brand', ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Apple', 'Other']) 
    
    # RAM
    ram = st.selectbox('RAM (GB)',[2, 4, 6, 8, 12, 16, 24, 32, 64])
    
    # Weight
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1)
    
    # Touchscreen
    touchscreen_input = st.selectbox('Touchscreen', ['No','Yes'])
    
    # Screen Size 
    screen_size = st.number_input('Screen Size (Inches)', min_value=10.0, max_value=18.0, value=13.3, step=0.1)
    
    # CPU Brand 
    cpu = st.selectbox('CPU Brand', ['Intel Core i7', 'Intel Core i5', 'Intel Core i3', 'AMD Processor', 'Other Intel Processor'])
    
    # HDD
    hdd = st.selectbox('HDD (GB)',[0, 500, 1000, 2000])

with col2:
    # Type of laptop
    type_name = st.selectbox('Type', ['Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook'])
    
    # IPS
    ips_input = st.selectbox('IPS Display', ['No','Yes'])
    
    # Resolution
    resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    
    # GPU Brand 
    gpu = st.selectbox('GPU Brand', ['Intel', 'Nvidia', 'AMD'])
    
    # OS
    os_input = st.selectbox('OS', ['Windows', 'Mac', 'Others/No OS/Linux'])
    
    # SSD
    ssd = st.selectbox('SSD (GB)',[0, 128, 256, 512, 1024, 2048])

st.markdown("---")

# Center the button
_, col_btn, _ = st.columns([1, 1, 1])

if col_btn.button('Predict Price', type='primary', use_container_width=True):
    
    # ----------------------------------------------------
    # 2. Feature Engineering 
    # ----------------------------------------------------
    
    # Converting Yes/No to 1/0
    touchscreen = 1 if touchscreen_input == 'Yes' else 0
    ips = 1 if ips_input == 'Yes' else 0

    # Calculating PPI
    try:
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
    except ZeroDivisionError:
        ppi = 0
    
    # Creating Input Dataframe
    data = {
        'Company': [company],
        'TypeName': [type_name], 
        'Ram': [ram],
        'Weight': [weight],
        'TouchScreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'CPU_Brand': [cpu], 
        'HDD': [hdd],
        'SSD': [ssd],
        'GPU_brand': [gpu], 
        'os': [os_input]
    }
    
    query_df = pd.DataFrame(data)

    try:
        # ----------------------------------------------------
        # 3. Prediction & Inverse Transformation
        # ----------------------------------------------------
        log_prediction = pipe.predict(query_df)
        actual_price = np.expm1(log_prediction)[0]
            
        # Formatting currency to Indian Style
        formatted_price = format_currency(actual_price, 'INR', locale='en_IN')
            
        # ----------------------------------------------------
        # 4. Display Result 
        # ----------------------------------------------------
        st.markdown(f"""
            <div style="text-align: center; padding: 10px;">
                <h3 style="margin-bottom: 0px;">The estimated price is:</h3>
                <h1 style="color: #4CAF50; font-size: 50px; margin-top: 0px;">{formatted_price}</h1>
            </div>
        """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)
        
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 0.9em; padding-top: 20px;'>
        <strong>Laptop Price Predictor</strong><br>
        Created by <a href='https://kindo-tk.github.io/tk.github.io/' target='_blank'>Tufan Kundu</a> ·
        <a href='https://github.com/kindo-tk' target='_blank'>GitHub</a> ·
        <a href='https://www.linkedin.com/in/tufan-kundu-577945221/' target='_blank'>LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)