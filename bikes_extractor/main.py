import time
import requests
import json
from pprint import pprint
import pandas as pd
import sqlalchemy
import pymysql
from sqlalchemy import create_engine

'''
Created by Conan Martin
13th March 2017
For Software Engineering Group Project - Dublin Bikes API
Team Infinite Loop: Conan Martin, Karl Roe, David Surridge.
Git: https://github.com/conanmartin/Dublin_Bikes

Bikes Extractor
For Scraping Dublin Bikes API
'''
# JCD API Key: b651d697e937e2cd75f21e3f5ce001ace26b4354


def bike_extract(file_name, print_output):
	bike_key = "b651d697e937e2cd75f21e3f5ce001ace26b4354"
	contract = "Dublin"
	dub_bikes_uri = "https://api.jcdecaux.com/vls/v1/stations"
	try:
		# connects to and downloads from the Dublin Bikes API
		r = requests.get(dub_bikes_uri, params={"apiKey": bike_key, "contract": contract})
		bike_data = json.loads(r.text)
		df = pd.DataFrame(bike_data)
		# timestamp is now human readable
		df['last_update'] = pd.to_datetime((df['last_update'] + 3600000) * 10e5)
		# removes columns not required
		clean_df = df[['number', 'last_update', 'available_bike_stands', 'available_bikes', 'status']]
		print(clean_df)

		# saves to csv
		df.to_csv(file_name, mode='a', header=False)
		if print_output:
			pprint(bike_data)

		# saves to mySQL database
		# creates temporary table with latest df, then adds non-existing rows to bikes_dynamic - this keeps out duplicates
		engine = create_engine("mysql+pymysql://DavidSurridge:MyGerryAdams@dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com:3306/myDublinBikes", echo = True)
		clean_df.to_sql(name='temp_table', con=engine, if_exists='replace', index=False)
		connection = engine.connect()
		connection.execute("INSERT INTO bikes_dynamic SELECT * FROM temp_table ON DUPLICATE KEY UPDATE bikes_dynamic.status=temp_table.status")
	except:
		# exception handling/error logging
		print("Error")
		error_time = str(time.time())
		f = open('error_log', 'a')
		f.write('\nError at: ' + error_time)
		f.close()
		pass


def main():
	run = 0
	while True:
		run += 1
		print(run)
		print("starting")
		bike_extract("dublin_bikes_output.csv", False)
		print("stopping")
		# Runs every 5 minutes
		time.sleep(300)

if __name__ == '__main__':
	main()
