import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# LOAD MODEL + ORIGINAL DATA
# -----------------------------

model = joblib.load("laptop_price_model.pkl")  
df = pd.read_csv("clean_laptop_data.csv")       # needed for dropdown items


st.title("💻 Laptop Price Prediction App")

st.write("Select laptop specifications and get the estimated price, along with similar laptop suggestions.")


# ------------------------------------
# BUILD INPUT FORM FOR ALL FEATURES
# ------------------------------------

# Categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Numerical columns
numerical_cols = df.select_dtypes(exclude=['object']).columns.tolist()
numerical_cols.remove("Price")   # remove target if present

user_data = {}

st.header("Laptop Specifications")

# -------------------------------
# 1. Categorical Inputs (Dropdown)
# -------------------------------

for col in categorical_cols:
    user_data[col] = st.selectbox(
        f"Select {col}",
        sorted(df[col].dropna().unique())
    )

# -------------------------------
# 2. Numerical Inputs
# -------------------------------

for col in numerical_cols:
    min_val = float(df[col].min())
    max_val = float(df[col].max())
    
    user_data[col] = st.number_input(
        f"Enter {col}",
        min_value=min_val,
        max_value=max_val,
        value=min_val
    )


# ---------------------------------
# Convert inputs → DataFrame
# ---------------------------------

input_df = pd.DataFrame([user_data])


# -------------------------------
# Predict Button
# -------------------------------

if st.button("Predict Price"):
    
    price = model.predict(input_df)[0]

    st.subheader(f"💰 Estimated Price: ₹ {price:,.0f}")

    # ---------------------------------------
    # FIND SIMILAR LAPTOPS
    # ---------------------------------------
    st.subheader("🔍 Similar Laptops You May Like")

    # Filter laptops with same category specs
    similar = df.copy()

    for col in categorical_cols:
        similar = similar[similar[col] == user_data[col]]

    # Sort by nearest price
    similar["Price_diff"] = abs(similar["Price"] - price)
    similar = similar.sort_values("Price_diff").head(4)

    st.table(similar[["Company", "TypeName", "CPU_Brand", "GPU_Brand", "Ram", "Weight", "Price"]])
