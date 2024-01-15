from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor


app = Flask(__name__)

# Assuming you have a function to make predictions using your time series model
def make_predictions():
    # Your time series prediction logic here
    # Return a pandas DataFrame with columns 'Date' and 'Prediction'
    dates = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
    predictions = np.random.rand(len(dates)) * 10
    df = pd.DataFrame({'Date': dates, 'Prediction': predictions})
    return df

@app.route('/')
def index():
    # Make predictions
    df_predictions = make_predictions()

    # Create a Plotly chart
    chart = px.line(df_predictions, x='Date', y='Prediction', title='Time Series Prediction')

    # Convert the Plotly chart to HTML
    chart_html = chart.to_html(full_html=False)

    return render_template('index.html', chart_html=chart_html)

if __name__ == '__main__':
    app.run(debug=True)
