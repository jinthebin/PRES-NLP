from application import app
from flask import render_template, url_for
import pandas as pd
import plotly
import plotly.express as px
import json
from sentiment import sentiment_analysis
from dataload import test_data
from .utils import auth_required

@app.route("/")
@auth_required
def index(): #call this method anything

    #Graph one
    df = px.data.medals_wide()
    fig1 = px.bar(df, x = "nation", y=['gold','silver','bronze'], title = "Wide=FormInput")
    graph1JSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)

    #graph2
    df2 = px.data.iris()
    fig2 = px.scatter_3d(df2, x = "sepal_length", y = "sepal_width", z = "petal_width",
                         color = "species", title = "Iris Dataset")
    
    graph2JSON = json.dumps(fig2, cls = plotly.utils.PlotlyJSONEncoder)

    # Graph three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4 - sentiment analysis using asent visualized
    figsent = sentiment_analysis(test_data['Text'])

    return render_template('index.html', title='Home', graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON=graph3JSON, figsent = figsent)

@app.route("/layout") #this is the hyperlink 
@auth_required
def layout():
    return render_template("layout.html", title= 'layout')