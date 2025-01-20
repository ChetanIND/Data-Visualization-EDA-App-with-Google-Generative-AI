
# Data Dashboard & EDA App with Google Generative AI

This Streamlit app allows you to visualize and explore your datasets in an interactive way. You can upload a CSV file to:
- View a preview of your dataset
- Generate various visualizations like scatter plots, bar charts, line charts, and histograms
- Generate an Exploratory Data Analysis (EDA) report using `ydata-profiling`
- Receive data preprocessing suggestions from Google Generative AI based on the EDA profile

## Features
1. **Data Dashboard**:
   - Upload a CSV file and view the dataset preview
   - Visualize your data using various chart types (scatter plot, bar chart, line chart, histogram)
   - Customizable chart settings (select X-axis, Y-axis, color, etc.)

2. **Exploratory Data Analysis (EDA)**:
   - Generate a comprehensive EDA report with detailed insights using `ydata-profiling`
   - Get data preprocessing suggestions from Google Generative AI based on the EDA profile

## Installation

### Prerequisites:
- Python 3.x
- Google Cloud API credentials for Generative AI access

### Required Libraries:
You need to install the following libraries:

```bash
pip install streamlit pandas plotly ydata-profiling streamlit-pandas-profiling google-generativeai
```

### Google Generative AI Setup:
1. Set up Google Cloud credentials by following [Google Cloud setup instructions](https://cloud.google.com/docs/authentication/getting-started).
2. Use the following command to authenticate:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_service_account_key.json"
```

## How to Run the App

1. Clone this repository:
```bash
git clone https://github.com/your-username/data-dashboard-eda-app.git
cd data-dashboard-eda-app
```

2. Run the app:
```bash
streamlit run app.py
```

3. Open your browser and go to `http://localhost:8501` to use the app.

## App Usage

1. **Data Dashboard**:
   - Upload a CSV file using the sidebar.
   - Choose the type of visualization you want to generate.
   - Select columns for your chart and see the interactive visualization.

2. **Exploratory Data Analysis (EDA)**:
   - Upload a CSV file to generate a profiling report of your dataset.
   - The app will provide an interactive report with summary statistics, missing values, and correlations.
   - Based on the EDA profile, Google Generative AI will suggest possible data preprocessing steps.

## Contributions

Feel free to contribute by forking the repository and submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Streamlit for creating a simple framework for building data apps
- `ydata-profiling` for EDA reports
- Plotly for interactive visualizations
- Google Generative AI for data preprocessing suggestions

## Demo [text](https://data-visualization-eda-app-with-app-generative-ai-cih.streamlit.app/)