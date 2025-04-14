from flask import Flask, render_template
import json
import ors_request
import street_view_request
# import geocoder

app = Flask(__name__)

with open('config.json') as f:
    keys = json.load(f)


@app.route('/')
def home():
    return render_template('map.html')

# the user inputs on UI need to go here as params
def inference_pipeline(start, end, keys):
    # dummy variables
    
    

if __name__ == '__main__':
    app.run(debug=True)
    # call inference_pipeline after getting input
