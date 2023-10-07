import os
import requests
from dotenv import load_dotenv


class WeatherChecker:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, city_name):
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'  # Temperature in Celsius
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    def check_temperature(self, city_name, min_temp, max_temp):
        weather_data = self.get_weather_data(city_name)

        if weather_data:
            temperature = weather_data['main']['temp']
            print(f"Current temperature in {city_name}: {temperature}°C")

            if temperature < min_temp:
                return f"Alert: Temperature is below {min_temp}°C"
            elif temperature > max_temp:
                return f"Alert: Temperature is above {max_temp}°C"
            else:
                return "Temperature is within the preferred range."
        else:
            return "Unable to check temperature. Please try again later."


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('API_KEY')

    if api_key is None:
        print("API_KEY not found in .env file.")
    else:
        weather_checker = WeatherChecker(api_key)

        city_name = input("Enter the name of your preferred location: ")
        min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
        max_temp = float(input("Enter the maximum temperature threshold (in °C): "))

        weather_checker.check_temperature(city_name, min_temp, max_temp)