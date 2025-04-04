import google_streetview.api
import json

with open("config.json") as f:
    data = json.load(f)
    key = data['GOOGLE_API_KEY']


def get(lat, long, heading, pitch):
 
    params = [{
        'size': '640x640',  # Max 640x640 pixels
        'location': '40.748817,-73.985428',
        'heading': '151.78',
        'pitch': '-0.76',
        'key': key
    }]

    # Create a results object
    results = google_streetview.api.results(params)

    # Download images to the current directory
    results.download_links('downloads')


get(1, 1, 1, 1)


