import time
import requests
import json
import flask
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize
import csv


def weather_extract(file_name, print_output):
	weather_key = "4cd167bc85dff937818ea9a5eb6fa550"
	city_id = "2964574"
	open_weather_uri = "http://api.openweathermap.org/data/2.5/weather"
	r = requests.get(open_weather_uri, params={"APPID": weather_key, "id": city_id, "units": "metric"})
	weather_data = json.loads(r.text)

	if print_output:
		pprint(weather_data)

	# result = json_normalize(weather_data, ['main', str('temp')])
	# pprint(result)
	with open(file_name, 'w') as f:
		json.dump(weather_data, f)
		f.write("\n")
	f.close()

	df = pd.read_json(file_name)
	print(df)

	# df = pd.DataFrame(weather_data)
	# df.to_csv("test_open_weather_output.csv", mode='a', header=False)

def run():
	weather_extract("test_open_weather_output.json", True)

run()
