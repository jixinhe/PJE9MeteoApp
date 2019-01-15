import requests
import json


class SourceData:
    #
    # to operate the information sent by OpenWeatherMap
    #
    def __init__(self):
        print('init SourceData')
        self.url = 'https://samples.openweathermap.org/data/2.5/forecast?q=paris&mode=json&appid=569888b222a36483ebec447fe0465a8a'

    def get_forecast(self):
        print('Get_forecast')
        fc_data = requests.get(self.url)
        self.city_id = fc_data['city']['id']
        self.city_name = fc_data['city']['name']
        print('City ' + self.city_name + ' whose ID is ' + str(self.city_id))
        data = fc_data.json()
        name = data['city']['name']
        return json.dumps(name)

