import googlemaps
import flask
import Math

gmaps = googlemaps.Client(key='AIzaSyC3ORJmeSdB-aN5pqWwypJ0Y9QeK_KnY0U')

# Address inputed by user
address = request.form['add']

# Geocoding an address
geocode_result = gmaps.geocode(address)

# Find closest sensor
class Sensor:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates


sensors = (
    Sensor('Pavilion Sensor', gmaps.geocode('The Pavilion Davis, CA 95616'))
)


def calc_distance(add1, add2):
    return Math.sqrt((add1[0] - add2[0]) **2 + (add1[1] - add2[1]) ** 2)


closest_sensor = sensors[0]
min_dist = calc_distance(address, sensors[0])
for s in sensors:
    dist = calc_distance(address, s)
    if(dist < min_dist):
        min_dist = dist
        closest_sensor = s

# Take measurements from sensor - make "prediction"
#temperature = 

if (temperature > 800): #in celcius
    render_template('DangerResult.html')
else:
    render_template('SafeResult.html')
# Tell user if they are in danger
