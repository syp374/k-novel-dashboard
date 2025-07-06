# utils/data_loader.py
import pandas as pd
import streamlit as st

@st.cache_data # Caches the data to avoid reloading on every interaction
def load_data(file_path):
    """
    Loads a CSV file from the specified path into a pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Error: The file was not found at {file_path}. Please make sure it's in the 'data' folder.")
        return pd.DataFrame() # Return empty dataframe on error
