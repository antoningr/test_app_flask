############################################################################################################
# Description: This is the main file for the web application with Flask 
# Author: 
# Date: 16/01/2023
# Version projet: 1.0
# Python Version: 3.11.1
# Flask Version: 2.2.2
############################################################################################################


# Importing the Flask module
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask("Data Engineering : Web Applications with Flask")

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)