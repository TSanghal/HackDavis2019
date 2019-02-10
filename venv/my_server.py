from flask import Flask
from flask import send_from_directory
from flask import request, url_for, redirect
import googlemaps
import Math


app = Flask(__name__, static_folder='')


@app.route('/home')
def hello_world():
    print("hitting hello world...")
    return send_from_directory(app.static_folder, 'FrontEnd.html')

@app.route('/gettemp')
def getTemperatureByLoc():
    address = request.args.get('loc')
    gmaps = googlemaps.Client(key='AIzaSyC3ORJmeSdB-aN5pqWwypJ0Y9QeK_KnY0U')
    geocode_result = gmaps.geocode(address)


    # compare location to some table which grabs temperature info

    # if temp > x , send_from_directory a file that shows that

    # otherwise, send other file

    # return send_from_directory(app.static_folder, 'DangerResult.html')

    # return redirect(url_for('getDangerResult'))
    # return app.send_static_file('DangerResult.html')

    return '150'


@app.route('/dangerresult')
def getDangerResult():
    return send_from_directory(app.static_folder, 'DangerResult.html')

@app.route('/saferesult')
def getSafeResult():
    return send_from_directory(app.static_folder, 'SafeResult.html')