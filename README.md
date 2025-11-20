# Laptop Price Prediction

This project predicts laptop prices using machine learning based on key hardware specifications.
It includes a clean dataset, preprocessing pipeline, trained ML model, and an interactive Streamlit application.

## Project Overview

The aim is to build a model that can estimate laptop prices using features such as:

Company

Type

Processor brand & series

RAM

Storage (SSD/HDD)

GPU brand & type

Operating System

Display PPI

Weight

The Streamlit app provides dropdown-based selection for every feature and predicts the price instantly.

## Project Structure

laptop-price-prediction/
│
├── clean_data.csv
├── notebook.ipynb
├── streamlit_app.py
├── requirements.txt
└── README.md


⚠️ Note: model.pkl is not included in the repository due to GitHub’s 25MB upload limit.

## Download Trained Model

The trained model is stored on Google Drive.
Download it and place the file in the project root folder.

## Download model.pkl:
https://drive.google.com/file/d/1wfhZ71XTtWbaq_FxvVp09SCu-oh3RiEM/view?usp=sharing

After downloading, the project structure should look like this:

laptop-price-prediction/
│
├── model.pkl
├── clean_data.csv
├── notebook.ipynb
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
1️⃣ Clone the repository
git clone https://github.com/yourusername/laptop-price-prediction.git

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run streamlit_app.py

## Model Details

Dataset cleaned & processed

Categorical features encoded

Train-test split used

Best model trained (Random Forest or chosen algorithm)

Model saved as model.pkl (Download link provided above)

## Author

Yuvraj Singh Shekhawat
