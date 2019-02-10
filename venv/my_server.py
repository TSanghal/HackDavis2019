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

    user_lat = geocode_result[0]['geometry']['location']['lat']
    user_lng = geocode_result[0]['geometry']['location']['lng']

    #List of all sensors - would eventually read from database.
    sensors = [
        ['Pavilion Sensor', gmaps.geocode('The Pavilion Davis, CA 95616')]
    ]

    #Calculates the distance between two pairs of coordinates.
    def calc_distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    #Find the sensor closest to the user.
    closest_sensor = sensors[0]
    sens_lat = closest_sensor[1][0]['geometry']['location']['lat']
    sens_lng = closest_sensor[1][0]['geometry']['location']['lng']
    min_dist = calc_distance(user_lat, user_lng, sens_lat, sens_lng)
    for s in sensors:
        s_lat = s[1][0]['geometry']['location']['lat']
        s_lng = s[1][0]['geometry']['location']['lng']
        dist = calc_distance(user_lat, user_lng, s_lat, s_lng)
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