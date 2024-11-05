import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Function to load data
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)  # CSV file only
        except Exception as e:
            st.error("Error loading file.")
            return None
        return df
    return None

# Function to display data overview
def display_data_info(df):
    st.subheader("Data Overview")
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")
    
    # Display column names and data types
    data_info = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes
    })
    st.dataframe(data_info)

# Function to handle null values
def handle_null_values(df, columns, method):
    if method == 'Remove':
        df.dropna(subset=columns, inplace=True)
    elif method == 'Fill with Mean':
        for col in columns:
            df[col].fillna(df[col].mean(), inplace=True)
    elif method == 'Fill with Median':
        for col in columns:
            df[col].fillna(df[col].median(), inplace=True)
    return df

# Function to detect outliers using IQR
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]
    return outliers

# Function to visualize the data
def visualize_data(df, columns, plot_type):
    st.subheader("Data Visualization")
    if plot_type == 'Scatter Plot':
        x = st.selectbox("Select X-axis:", columns)
        y = st.selectbox("Select Y-axis:", columns)
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[x], y=df[y])
        st.pyplot(plt)
    elif plot_type == 'Histogram':
        col = st.selectbox("Select Column:", columns)
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True)
        st.pyplot(plt)
    elif plot_type == 'Box Plot':
        col = st.selectbox("Select Column:", columns)
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[col])
        st.pyplot(plt)

# Main Streamlit App
st.title("Data Preprocessing and Visualization Pipeline")

# Step 1: File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
df = load_data(uploaded_file)

if df is not None:
    # Step 2: Display Data Overview
    display_data_info(df)
    
    # Step 3: Choose Preprocessing Options
    st.subheader("Preprocessing Options")
    columns = st.multiselect("Select Columns for Preprocessing:", df.columns)
    
    # Null value handling
    null_method = st.selectbox("Handle Null Values:", ["None", "Remove", "Fill with Mean", "Fill with Median"])
    if null_method != "None" and len(columns) > 0:
        df = handle_null_values(df, columns, null_method)
    
    # Outlier detection and removal
    if st.checkbox("Detect and Remove Outliers"):
        outlier_col = st.selectbox("Select Column for Outlier Detection:", df.columns[df.dtypes != 'object'])
        outliers = detect_outliers(df, outlier_col)
        st.write("Outliers Detected:")
        st.dataframe(outliers)
        remove_outliers = st.checkbox("Remove Outliers")
        if remove_outliers:
            df = df[~df.index.isin(outliers.index)]

    # Step 4: Visualize Data
    st.subheader("Data Visualization")
    plot_type = st.selectbox("Select Plot Type:", ["Scatter Plot", "Histogram", "Box Plot"])
    visualize_data(df, df.columns, plot_type)