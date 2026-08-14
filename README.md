# dashboard

# CSV Explorer

A simple desktop GUI tool built with Python and tkinter to explore CSV files.

## What it does

- Load any CSV file through a file picker
- View the list of columns in the file
- Pick a column and a chart type (bar, line, or scatter)
- See the chart rendered live inside the app
- View quick summary stats (mean, min, max, count) for the selected column

## Built with

- Python
- tkinter (GUI)
- pandas (data handling)
- matplotlib (charts)

## How to run

1. Make sure you have Python installed
2. Install the required libraries:
   ```
   pip install pandas matplotlib
   ```
3. Run the app:
   ```
   python dashboard.py
   ```
4. Click **Load CSV**, pick a file, choose a column and chart type, then click **Plot**

## About this project

This was built as a hands-on way to learn tkinter — window setup, widgets, layout,
event binding, and embedding matplotlib charts inside a GUI window.
