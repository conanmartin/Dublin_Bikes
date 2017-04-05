'''
Created on 31 Mar 2017
 
@authors: David, Conan, Karl
'''

from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
import pymysql 
import simplejson as json
from pprint import pprint
app =Flask(__name__, static_url_path='')


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
	rows = conn.execute("SELECT * from bikes_static")
	for row in rows:
		stations.append(dict(row))

	return jsonify(stations=stations)

@app.route("/available/<int:station_id>")
def get_dynamic_stations(station_id):
	engine = connect_to_database()
	conn = engine.connect()
	data = []
	rows = conn.execute("SELECT available_bikes from bikes_dynamic where number = {};".format(station_id))
	for row in rows:
		data.append(dict(row))

	return jsonify(available=data)

if __name__ == "__main__":
	app.run()
