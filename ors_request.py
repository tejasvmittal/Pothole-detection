import openrouteservice
from openrouteservice import convert
import json
import math

with open('config.json') as f:
    data = json.load(f)
    key = data['OPEN_ROUTE_SERVICE_API_KEY']


def get(start_lat, start_long, end_lat, end_long):
    # implement getting an single alternative route as well

    coords = ((start_long, start_lat), (end_long, end_lat))
    client = openrouteservice.Client(key=key) 
    # decode_polyline needs the geometry only
    route_params = {
    "coordinates": coords,
    "profile": 'driving-car',
    "format": "geojson",
    "instructions": False
}
    routes = client.directions(**route_params)
    all_routes_coordinates = []
    for route in routes['features']:
        # Extract the encoded polyline geometry
        geometry = route['geometry']
        all_routes_coordinates.append(geometry['coordinates'])
    return all_routes_coordinates


def calculate_heading(lat1, lon1, lat2, lon2):
    """
    Generate n-1 headings, each heading will be paired with 
    the initial coordinate for that heading
    """
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    x = math.sin(dLon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(dLon))
    heading = math.degrees(math.atan2(x, y))
    return (heading + 360) % 360  # Normalize


if __name__ == '__main__':
    r = get(33.763989, -118.165501, 33.770049, -118.193658)
    flattened_coords = [coord for route in r for coord in route]
    print(flattened_coords)
