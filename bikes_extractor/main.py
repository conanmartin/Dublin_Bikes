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
Git: https://github.com/DavidSurridge/DublinBikes.git
'''
'''
Bikes Extractor
For Scraping Dublin Bikes API
'''
# JCD API Key: b651d697e937e2cd75f21e3f5ce001ace26b4354


def bike_extract(file_name, print_output):
	bike_key = "b651d697e937e2cd75f21e3f5ce001ace26b4354"
	contract = "Dublin"
	dub_bikes_uri = "https://api.jcdecaux.com/vls/v1/stations"
	#API request
	try:
		r = requests.get(dub_bikes_uri, params={"apiKey": bike_key, "contract": contract})
	except:
		pass

	bike_data = json.loads(r.text)
	df = pd.DataFrame(bike_data)
	df['last_update'] = pd.to_datetime((df['last_update'] + 3600000) * 10e5)
	clean_df = df[['number', 'last_update', 'available_bike_stands', 'available_bikes', 'status']]
	print(clean_df)

	#to csv
	df.to_csv(file_name, mode='a', header=False)
	if print_output:
		pprint(bike_data)

	# to mySQL
	dburi = 'dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com'
	db = 'Dublin_bikes'
	username = 'DavidSurridge'
	port = '3306'
	password = 'MyGerryAdams'
	print(df['status'])

	engine = create_engine("mysql+pymysql://DavidSurridge:MyGerryAdams@dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com:3306/myDublinBikes", echo = True)
	clean_df.to_sql(name='bikes_dynamic', con=engine, if_exists='append', index=False)


def main():
	# while True:
	bike_extract("dublin_bikes_output.csv", False)
	#Runs every 5 minutes
	# time.sleep(300)

if __name__ == '__main__':
	main()
