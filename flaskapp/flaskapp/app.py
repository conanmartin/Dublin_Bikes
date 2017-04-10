'''
Created on 31 Mar 2017
 
@authors: team 1. David, Conan, Karl 
'''

from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
import pymysql 
import simplejson as json
from pprint import pprint
app = Flask(__name__, static_url_path='')


@app.route("/")
def hello():
    return render_template("index.html")
    
def connect_to_database():
    engine = create_engine("mysql+pymysql://DavidSurridge:MyGerryAdams@dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com:3306/myDublinBikes", echo = False)
    return engine

@app.route("/stations")
def get_stations():
    engine = connect_to_database()
    conn = engine.connect()
    stations = []
    rows = conn.execute("SELECT * from bikes_static ORDER BY address;")
    for row in rows:
        stations.append(dict(row))

    return jsonify(stations=stations)

@app.route("/available_weekly/<int:station_id>")
def get_dynamic_stations(station_id):
    engine = connect_to_database()
    conn = engine.connect()
    data = []
    rows = conn.execute("SELECT dayofweek(last_update), avg(available_bikes) as avg_bikes from bikes_dynamic where time(last_update) > '05:00:00' and number = {} group by dayofweek(last_update);".format(station_id))
    for row in rows:
        data.append(dict(row))

    return jsonify(available=data)

@app.route("/available_daily/<int:station_id>/<int:day_num>")
def get_daily_stations(station_id, day_num):
    engine = connect_to_database()
    conn = engine.connect()
    data = []
    rows = conn.execute("SELECT hour(last_update), avg(available_bikes) as avg_bikes from myDublinBikes.bikes_dynamic where hour(last_update) > 5 and number = {} and dayofweek(last_update) ={} group by hour(last_update);".format(station_id, day_num))
    for row in rows:
        data.append(dict(row))

    return jsonify(available=data)


if __name__ == "__main__":
    app.run()