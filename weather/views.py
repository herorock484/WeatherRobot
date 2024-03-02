from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e49bef7606d0c4345c75fa9a4e64f17e'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    return render(request, 'weather/index.html') #returns the index.html template