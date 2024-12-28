import streamlit as st
import pandas as pd
import google.generativeai as genai
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly.express as px
import os

genai.configure(api_key="AIzaSyDTw3flfdqAbGDU3xFxkeInBQIObfvuG2s")

# Initialize the Google Generative AI client
client = genai.GenerativeModel("gemini-1.5-flash")

# App configuration
st.set_page_config(page_title="Data Dashboard & EDA App with Google Generative AI", layout="wide")

# Sidebar for navigation
st.sidebar.title("App Navigation")
page = st.sidebar.radio("Select a Page", ["Data Dashboard", "Exploratory Data Analysis (EDA)"])

# Main title
st.title("📊 Data Dashboard & EDA App with Google Generative AI")
st.markdown("""
Welcome to the Data Dashboard and EDA App! You can either visualize your data or generate detailed profiling reports based on the dataset you upload.
""")

# File upload section
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Function to get preprocessing suggestions from Google Generative AI
def get_generative_ai_suggestions(eda_profile):
    prompt = f"Based on the following Exploratory Data Analysis profile, suggest data preprocessing steps:\n{eda_profile}"

    # Get the response from Google Generative AI
    response = client.generate_content(prompt)

    # Extract the generated text (preprocessing suggestions)
    return response.text

# Page 1: Data Dashboard
if page == "Data Dashboard":
    if uploaded_file:
        try:
            # Read the uploaded file into a DataFrame
            df = pd.read_csv(uploaded_file)

            # Dataset preview
            st.subheader("Preview of Uploaded Dataset")
            st.dataframe(df.head())

            # Sidebar for column selection
            st.sidebar.header("Visualization Settings")
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            categorical_columns = df.select_dtypes(include=['object', 'category']).columns

            # Visualization options
            plot_type = st.sidebar.selectbox("Select Visualization Type", ["Scatter Plot", "Bar Chart", "Line Chart", "Histogram"])

            if plot_type == "Scatter Plot":
                x_axis = st.sidebar.selectbox("Select X-axis", options=numeric_columns)
                y_axis = st.sidebar.selectbox("Select Y-axis", options=numeric_columns)
                color = st.sidebar.selectbox("Select Color", options=categorical_columns)
                fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title="Scatter Plot")
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Bar Chart":
                x_axis = st.sidebar.selectbox("Select X-axis", options=categorical_columns)
                y_axis = st.sidebar.selectbox("Select Y-axis", options=numeric_columns)
                fig = px.bar(df, x=x_axis, y=y_axis, title="Bar Chart")
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Line Chart":
                x_axis = st.sidebar.selectbox("Select X-axis", options=numeric_columns)
                y_axis = st.sidebar.selectbox("Select Y-axis", options=numeric_columns)
                fig = px.line(df, x=x_axis, y=y_axis, title="Line Chart")
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Histogram":
                column = st.sidebar.selectbox("Select Column", options=numeric_columns)
                fig = px.histogram(df, x=column, title="Histogram")
                st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Error loading the file: {e}")
    else:
        st.sidebar.info("Please upload a CSV file to proceed.")
        st.write("### Awaiting Dataset Upload")
        st.markdown("Once you upload a dataset, you'll see a preview and visualization options here.")

# Page 2: Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis (EDA)":
    if uploaded_file:
        try:
            # Read the uploaded file into a DataFrame
            df = pd.read_csv(uploaded_file)

            # Dataset preview
            st.subheader("Preview of Uploaded Dataset")
            st.dataframe(df.head())

            # Generate EDA report using pandas-profiling
            st.subheader("Generating Profiling Report...")
            profile = ProfileReport(df, explorative=True)

            # Display profiling report
            st_profile_report(profile)

            # Get Google Generative AI's data preprocessing suggestions
            eda_profile = profile.to_json()
            suggestions = get_generative_ai_suggestions(str(eda_profile))

            # Display suggestions
            st.subheader("Google Generative AI's Data Preprocessing Suggestions")
            st.write(suggestions)

        except Exception as e:
            st.error(f"Error loading the file: {e}")
    else:
        st.sidebar.info("Please upload a CSV file to proceed.")
        st.write("### Awaiting Dataset Upload")
        st.markdown("Once you upload a dataset, you'll see a preview and the profiling report generated here.")
