# app.py

import requests

def get_current_weather(city):
    api_key = 'API KEY INSERT HERE'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    # Change the units parameter to 'imperial' for Fahrenheit
    params = {'q': city, 'appid': api_key, 'units': 'imperial'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            return {'error': 'Failed to fetch weather data. Please try again later.'}
    except Exception as e:
        return {'error': str(e)}

# Testing the function
if __name__ == '__main__':
    city_name = input("Enter city name: ")
    weather_data = get_current_weather(city_name)
    if 'error' in weather_data:
        print("Error:", weather_data['error'])
    else:
        print("Weather in", city_name)
        # Display temperature in Fahrenheit
        print("Temperature:", weather_data['temperature'], "°F")
        print("Humidity:", weather_data['humidity'], "%")
        print("Description:", weather_data['description'])
        print("Wind Speed:", weather_data['wind_speed'], "m/s")