from flask import (Flask, render_template, jsonify, request, redirect)
import os
import logging

# Get the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)



#################################################
# Flask Setup
#################################################
application = Flask(__name__)

#################################################
# Routes
#################################################

# create route that renders index.html template
@application.route("/")
def home():
    return render_template("index.html")
    
#################################################
# Run the application
#################################################

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()