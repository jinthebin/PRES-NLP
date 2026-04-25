from application import app
from flask import render_template

@app.route("/")
def index(): #call this method anything
    return render_template('index.html', title='index')

@app.route("/layout") #this is the hyperlink 
def layout():
    return render_template("layout.html", title= 'layout')