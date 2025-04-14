import ors_request
import street_view_request

route_coordinates = ors_request.get(33.712666, -117.773041, 33.704636, -117.763832)
flattened_coords = [coord for route in route_coordinates for coord in route]
print(flattened_coords)
for i in range(len(flattened_coords)-1):
    heading = ors_request.calculate_heading(flattened_coords[i][1], flattened_coords[i][0],
                                                flattened_coords[i+1][1], flattened_coords[i+1][0])
    street_view_request.get(flattened_coords[i][1], flattened_coords[i][0], heading, -10, i)

