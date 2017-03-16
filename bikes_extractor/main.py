import time
import requests
import json
import flask
from pprint import pprint
import pandas as pd
import csv

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
	r = requests.get(dub_bikes_uri, params={"apiKey": bike_key, "contract": contract})
	bike_data = json.loads(r.text)
	df = pd.DataFrame(bike_data)
	df.to_csv(file_name, mode='a', header=False)
	if print_output:
		pprint(bike_data)


def main():
	while True:
		bike_extract("dublin_bikes_output.csv", False)
		#Runs every 5 minutes
		time.sleep(300)

if __name__ == '__main__':
	main()
