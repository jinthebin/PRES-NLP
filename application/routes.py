from application import app
from flask import render_template, request, redirect, url_for, session
import pandas as pd
pd.options.plotting.backend = "plotly"
import plotly
import plotly.express as px
import json
from sentiment import sentiment_analysis
from dataload import test_data, sentiment_data
from .utils import auth_required
import pyLDAvis
from topicmodeling import topic_modeling_pipeline
from word_cloud import update_word_cloud

@app.route("/")
@auth_required
def index(): #call this method anything

    #Graph one

    sentiment_counts = sentiment_data.groupby(["Reporting Year", "Sentiment Label"]).size().reset_index(name='Count')
    fig1 = px.line(sentiment_counts, x="Reporting Year", y="Count", color="Sentiment Label",
                labels={'Count': 'Number of Responses', 'Reporting Year': 'Reporting FY'},
                title='Number of responses Over Time by Sentiment')
    fig1.update_layout(
        legend_title='Sentiment',
        plot_bgcolor='black',  # Set plot background color to black
        paper_bgcolor='black',  # Set paper background color to black
        font=dict(color='white')  # Set font color to white
    )

    graph1JSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)

    #graph2
    
    # fig2 = sentiment_data['Sentiment Label'].plot(kind = 'hist')
    sentiment_counts_small = sentiment_data.groupby("Sentiment Label").size().reset_index(name='Count')
    fig2 = px.pie(sentiment_counts_small, values="Count", names="Sentiment Label", hole=.3)
    graph2JSON = json.dumps(fig2, cls = plotly.utils.PlotlyJSONEncoder)

    # Graph three
    fig3 = px.histogram(sentiment_data, color='Sentiment Label', x="RRDN match using Trust ODS code", title='Number of responses over regions by Sentiment')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 4 - sentiment analysis using asent visualized
    plot_url = update_word_cloud(test_data, 'Text')

    return render_template('index.html', title='Home', graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON=graph3JSON, plot_url = plot_url)

@app.route("/layout") #this is the hyperlink 
@auth_required
def layout():
    return render_template("layout.html", title= 'layout')

@app.route("/presentation")
@auth_required
def presentation():
    return render_template("presentation.html", title = "presentation")

@app.route("/presentation3")
@auth_required
def presentation3():
    return render_template("presentation_3.html", title = "presentation3")

@app.route("/presentation2")
@auth_required
def presentation2():
    return render_template("presentation2.html", title = "presentation2")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "user1" and password == "pass":
            session['is_logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials. Please try again."
            
    return render_template('login.html', title='Login', error=error)

@app.route("/logout")
def logout():
    session.pop('is_logged_in', None)
    return redirect(url_for('login'))

@app.route("/TopicModeling")
@auth_required
def TopicModeling():
        # Generate HTML 
    vis_data = topic_modeling_pipeline(sentiment_data,20)
    vis_html = pyLDAvis.prepared_data_to_html(vis_data)
    
    return render_template('topic.html', title='Topic Modeling', pyldavis_html=vis_html)