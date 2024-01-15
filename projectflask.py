from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit

app = Flask(__name__,template_folder='template')




@app.route("/")
def  home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)