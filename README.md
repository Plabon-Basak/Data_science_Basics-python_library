# Data Science Basics — Python Library

A collection of beginner-to-intermediate Python projects demonstrating core data science and data engineering concepts: data cleaning, visualization, real-time APIs, and numerical computing.

---

## Projects

### Data Cleaner (`Data_cleaner_app/Day44/`)
A CLI tool that ingests raw CSV files, drops rows with missing values and duplicates, then saves the cleaned output.
python day44.py
 Enter input CSV path → Enter output CSV path
### Sales Report Analyzer (Sales_report_analyzer/)
Loads sales transaction data, cleans it (handles missing values, adds year-month and revenue columns), prints monthly totals and the top 5 products by revenue, and renders a bar chart.
python app.py
 Enter path to CSV (sample included)
### Temperature Plotter (Temperature_plotter/)
Reads daily temperature CSV data, computes a 7-day rolling average, detects anomalies using the robust IQR method, and annotates each outlier on the plot. Supports saving to PNG.
python app.py
Enter CSV path → Save plot (yes/no)
### Graph Plotter (graph_plotter_app/)
Choose between line, bar, or scatter plot. Enter data manually or load from a CSV file. Optionally save the rendered graph.
python day45.py
Choose graph type → Choose data source → Optionally save
### Global Weather Dashboard (Global_weather_dashboard.py)
CLI dashboard powered by the OpenWeatherMap API. View current weather for any city or compare temperatures across multiple cities in a bar chart.
python Global_weather_dashboard.py
View single city weather or compare multiple cities
### Stock Price Tracker (Stock_price_tracker.py)
Polls the Yahoo Finance JSON API for a given stock ticker at a configurable interval, printing the live price to the console.
python Stock_price_tracker.py
Enter ticker (e.g., AAPL) → Enter interval in seconds
### Matrix Calculator (matrics_calculator.py)
NumPy-based CLI calculator: enter two matrices and run addition, subtraction, element-wise multiplication, dot product, transpose, determinant, and inverse.
python matrics_calculator.py
Enter dimensions and elements for both matrices
Requirements
pip install pandas matplotlib requests beautifulsoup4 numpy
### License
This repository is open source and available under the MIT License (LICENSE).
