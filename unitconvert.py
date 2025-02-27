import streamlit as st
from pint import UnitRegistry
import time
import streamlit.components.v1 as components

# Initialize Unit Registry
ureg = UnitRegistry()

# Custom CSS with Animation
st.markdown("""
    <style>
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        .stApp {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            animation: fadeIn 1s ease-in;
        }
        .stButton>button {
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit App Title
st.title("🌟Unit Converter")

# Unit Categories
unit_categories = {
    "Length": ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile'],
    "Weight": ['milligram', 'gram', 'kilogram', 'pound', 'ounce'],
    "Temperature": ['celsius', 'fahrenheit', 'kelvin'],
    "Volume": ['milliliter', 'liter', 'cup', 'pint', 'quart', 'gallon'],
    "Speed": ['meter/second', 'kilometer/hour', 'mile/hour', 'knot'],
    "Time": ['seconds', 'minutes', 'hours', 'days'],
    "Pressure": ['pascal', 'bar', 'psi', 'atm'],
    "Energy": ['joule', 'calorie', 'kilojoule', 'kilocalorie'],
    "Power": ['watt', 'kilowatt', 'horsepower'],
    "Data": ['bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte']
}

# Select Conversion Category
category = st.selectbox("Select Category:", list(unit_categories.keys()))

# User Input Section
user_input = st.number_input("Enter Value:", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From Unit:", unit_categories[category])
to_unit = st.selectbox("To Unit:", unit_categories[category])

# Conversion Logic
if st.button("Convert"):
    try:
        with st.spinner("Converting..."):
            time.sleep(1)  # Simulate processing time
            converted_value = (user_input * ureg(from_unit)).to(to_unit)
            st.success(f"Converted Value: {round(converted_value.magnitude, 4)} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")

# Reset Button
if st.button("Reset"):
    st.rerun()

# Footer Animation
components.html("""
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(() => {
                let footer = document.createElement("div");
                footer.innerHTML = "<p style='text-align:center; font-weight:bold;'></p>";
                document.body.appendChild(footer);
            }, 2000);
        });
    </script>
""", height=50)
