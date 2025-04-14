import google_streetview.api
import json
import os
import requests

with open("config.json") as f:
    data = json.load(f)
    key = data['GOOGLE_API_KEY']

def get(lat, lon, heading=0, pitch=0, index=0):
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "640x640",
        "location": f"{lat},{lon}",
        "heading": str(heading),
        "pitch": str(pitch),
        "fov": "60",
        "key": key
    }

    response = requests.get(base_url, params=params)
    # Make sure the downloads folder exists
    os.makedirs("downloads", exist_ok=True)
    # Save image to disk with a unique filename
    filename = f"downloads/image_{index:04}.jpg"
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Saved: {filename}")

if __name__ == '__main__':
    get(40.748817, -73.985428, 0, -10)


