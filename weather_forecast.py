import requests
from pprint import pprint

def get_forecast(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=d651f7a4caa1d8e01f1687fc34a352a5"

    response = requests.get(url)

    # response.json() - 
    data = response.json()
    temperature = round(data['main']['temp'] - 273.15 ,2)
    weather_desc = data['weather'][0]['description'].title()
    
    return [temperature, weather_desc]


var = "Bulacan"
data = get_forecast(var)

temp = data[0]
desc = data[1]

print(temp)
print(desc)
