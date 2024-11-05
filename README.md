# Data Analysis and Visualization Pipeline Using Streamlit

## Project Overview
This project provides a user-friendly, interactive pipeline for data analysis and visualization, built with Python and Streamlit. Designed to streamline the data exploration process, this tool allows users to upload datasets, preprocess data, and generate insightful visualizations in a single, cohesive workflow. With its accessible interface, the pipeline enables users with varying technical skills to uncover data patterns, clean their data, and make data-driven decisions.

## Features
- **File Upload**: Supports easy uploading of CSV files for immediate analysis.
- **Data Overview**: Displays key information about the dataset, including the number of rows, columns, and data types.
- **Preprocessing Options**:
  - Handle missing values (remove, fill with mean/median).
  - Detect and remove outliers based on the Interquartile Range (IQR) method.
- **Data Visualization**:
  - Scatter plots, histograms, and box plots for data exploration.
  - Real-time, interactive updates based on user selections.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository-link.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository-name
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run test.py
   ```

## Usage
1. Launch the Streamlit app and upload a CSV file to start.
2. View the data overview to understand the dataset’s structure.
3. Choose preprocessing options such as handling missing values and outliers.
4. Select visualization options to explore relationships, distributions, and anomalies in your data.

## Project Structure
- **test.py**: Main script containing functions for data loading, preprocessing, and visualization.
- **requirements.txt**: List of required Python packages for the project.

## Future Enhancements
- Additional preprocessing options (e.g., normalization, encoding for categorical data).
- More advanced visualizations and analysis options.
- Export feature for processed data and generated visualizations.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any improvements.
