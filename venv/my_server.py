from flask import Flask
from flask import send_from_directory
from flask import request, url_for, redirect
import googlemaps
import math


app = Flask(__name__, static_folder='')


@app.route('/home')
def hello_world():
    return send_from_directory(app.static_folder, 'FrontEnd.html')

@app.route('/gettemp')
def getTemperatureByLoc():
    #Get address inputted by user.
    address = request.args.get('loc')
    gmaps = googlemaps.Client(key='AIzaSyC3ORJmeSdB-aN5pqWwypJ0Y9QeK_KnY0U')

    #Convert address into coordinates.
    geocode_result = gmaps.geocode(address)

    #List of all sensors - would eventually read from database.
    sensors = [
        ['Pavilion Sensor', gmaps.geocode('The Pavilion Davis, CA 95616')]
    ]

    #Calculates the distance between two pairs of coordinates.
    def calc_distance(add, sens):
        return math.sqrt((add[0] - sens[1]) ** 2 + (add[1] - sens[1]) ** 2)

    #Find the sensor closest to the user.
    closest_sensor = sensors[0]
    min_dist = calc_distance(geocode_result, sensors[0])
    for s in sensors:
        dist = calc_distance(geocode_result, s)
        if dist < min_dist:
            min_dist = dist
            closest_sensor = s

    #Would eventually read temperature from closest_sensor - currently hardcoded.
    temperature = str(850)
    return temperature

@app.route('/dangerresult')
def getDangerResult():
    return send_from_directory(app.static_folder, 'DangerResult.html')

@app.route('/saferesult')
def getSafeResult():
    return send_from_directory(app.static_folder, 'SafeResult.html')