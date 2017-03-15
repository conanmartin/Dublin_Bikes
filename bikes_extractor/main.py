'''
Created by Conan Martin
13th March 2017
For Software Engineering Group Project - Dublin Bikes API
Team Infinite Loop: Conan Martin, Karl Roe, David Surridge.
Git: https://github.com/DavidSurridge/DublinBikes.git
'''
'''
Extractor
For Scraping Dublin Bikes and OpenWeatherMap APIs
'''
# JCD API Key: b651d697e937e2cd75f21e3f5ce001ace26b4354
# OpenWeatherMap API Key: 4cd167bc85dff937818ea9a5eb6fa550
import time
import requests
import json
import flask
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize


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



def weather_extract(file_name, print_output):
    weather_key = "4cd167bc85dff937818ea9a5eb6fa550"
    city_id = "2964574"
    open_weather_uri = "http://api.openweathermap.org/data/2.5/weather"
    r = requests.get(open_weather_uri, params={"APPID": weather_key, "id": city_id, "units": "metric"})
    weather_data = json.loads(r.text)
    if print_output:
        pprint(weather_data)
    # result = json_normalize(weather_data, 'main[0]')
    # print(result)
    with open(file_name, 'w') as f:
        json.dump(weather_data, f)
    # weather_df = pd.DataFrame(weather_data)
    # weather_df.to_csv(file_name, mode='a', header=False)




def main():
    # bike_extract("dublin_bikes_output.csv", True)
    weather_extract("open_weather_outputjson.json", True)

if __name__ == '__main__':
    main()
