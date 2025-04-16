from flask import Flask, request, jsonify
from flask_cors import CORS  
import ors_request

app = Flask(__name__)
CORS(app, resources={r"/get-route": {"origins": "http://127.0.0.1:5500"}})


@app.route('/get-route', methods=['POST'])
def get_route():
    data = request.get_json()
    lat1 = data.get('lat1')
    lng1 = data.get('lng1')
    lat2 = data.get('lat2')
    lng2 = data.get('lng2')
    route_coordinates = ors_request.get(lat1, lng1, lat2, lng2)
    flattened_coords = [coord for route in route_coordinates for coord in route]
    return jsonify({'route': flattened_coords})

if __name__ == '__main__':
    app.run(debug=True)