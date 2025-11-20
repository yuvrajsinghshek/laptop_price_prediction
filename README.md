# Laptop Price Prediction

A machine learning project that predicts laptop prices based on their technical specifications.
This project includes complete data cleaning, feature engineering, model training, and a Streamlit-based interactive interface that allows users to predict prices by selecting specifications from dropdown menus.

## Project Overview

This project aims to build a supervised machine learning model that accurately estimates laptop prices using key features such as:

Company,
Type,
Processor Series,
RAM,
Storage,
GPU,
Operating System,
Display Features,
Weight

The Streamlit web application provides an intuitive interface for users to select specifications and instantly view predicted laptop prices.

## Project Structure

laptop-price-prediction/
│
├── clean_data.csv
├── notebook.ipynb
├── model.pkl
├── streamlit_app.py
├── requirements.txt
└── README.md

## Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

## How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/laptop-price-prediction.git

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit Application
streamlit run streamlit_app.py

## Model Details

Dataset cleaned and preprocessed

Categorical features encoded

Train-test split applied

Best-performing model selected (RandomForest or chosen model)

Model saved as model.pkl using pickle

## Key Features

✔ Clean and well-processed dataset

✔ Accurate ML model for price prediction

✔ User-friendly Streamlit interface

✔ Dropdown-based selection for each laptop specification

✔ Production-ready and fully deployable

## Author

Yuvraj Singh Shekhawat
