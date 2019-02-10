import googlemaps
import flask
import Math

# Find closest sensor
class Sensor:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates


def calc_distance(add1, add2):
    return Math.sqrt((add1[0] - add2[0]) **2 + (add1[1] - add2[1]) ** 2)


# Take measurements from sensor - tell user if in danger or not
def measure_result():
    temperature = 850
    if temperature > 800:  #in Celcius
        danger = 1
    else:
        danger = 0


def main():
    gmaps = googlemaps.Client(key='AIzaSyC3ORJmeSdB-aN5pqWwypJ0Y9QeK_KnY0U')

    # Address inputted by user
    address = request.form['add']

    # Geo-coding an address
    geocode_result = gmaps.geocode(address)

    sensors = (
        Sensor('Pavilion Sensor', gmaps.geocode('The Pavilion Davis, CA 95616'))
    )

    closest_sensor = sensors[0]
    min_dist = calc_distance(geocode_result, sensors[0])
    for s in sensors:
        dist = calc_distance(geocode_result, s)
        if dist < min_dist:
            min_dist = dist
            closest_sensor = s
    measure_result()
