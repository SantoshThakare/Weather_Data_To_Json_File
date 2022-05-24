import requests
import json
import time

city_list = ["mumbai", "pune", "jalgaon", "surat", "bengaluru", "goa", "nagpur"]

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

weather_data = {'weather': []}


def read_file():
    with open('weather.json', 'r') as file_:
        try:
            old_data = json.load(file_)
        except json.decoder.JSONDecodeError:
            return weather_data
        return old_data


def write_file(data):
    old_data = read_file()
    print('writing data into file.')
    with open('weather.json', 'w') as file_:
        old_data['weather'].append(data)
        json.dump(old_data, file_, indent=2)


def get_weather(city):
    url = api_address + city
    print(f'Getting weather report for city : {city}')
    response = requests.get(url)
    response = response.json()
    response['main']['city'] = city
    write_file(response['main'])


def main(cities):
    for city in cities:
        get_weather(city)


if __name__ == '__main__':
    start_time = time.countertime()
    main(city_list)
    end_time = time.countertime()
    timedelta = end_time - start_time
    print(timedelta)
