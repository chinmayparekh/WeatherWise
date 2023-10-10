import os
import requests
from dotenv import load_dotenv


# Create a WeatherChecker class to handle weather api-related tasks
class WeatherChecker:
    def __init__(self, api_key):
        self.api_key = api_key

    # Method to fetch weather data for a given city
    def get_weather_data(self, city_name):
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'  # Temperature in Celsius
        }

        # Send a GET request to the OpenWeatherMap API
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            # If the response is successful, parse the JSON data and return it
            data = response.json()
            return data
        else:
            # If the response is not successful, print an error message and return None
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    # Method to check if the current temperature is within a specified range
    def check_temperature(self, city_name, min_temp, max_temp):
        # Get weather data for the specified city
        weather_data = self.get_weather_data(city_name)

        if weather_data:
            # Extract the temperature from the weather data
            temperature = weather_data['main']['temp']
            print(f"Current temperature in {city_name}: {temperature}°C")

            # Compare the temperature with the specified thresholds
            if temperature < min_temp:
                return f"Alert: Temperature is below {min_temp}°C"
            elif temperature > max_temp:
                return f"Alert: Temperature is above {max_temp}°C"
            else:
                return "Temperature is within the preferred range."
        else:
            return "Unable to check temperature. Please try again later."


# Main program entry point
if __name__ == "__main__":
    # Load API key from a .env file using dotenv
    load_dotenv()
    api_key = os.getenv('API_KEY')

    if api_key is None:
        print("API_KEY not found in .env file.")
    else:
        # Create an instance of the WeatherChecker class with the API key
        weather_checker = WeatherChecker(api_key)

        # Prompt the user for input
        city_name = input("Enter the name of your preferred location: ")
        min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
        max_temp = float(input("Enter the maximum temperature threshold (in °C): "))

        # Call the check_temperature method to check the weather conditions
        weather_checker.check_temperature(city_name, min_temp, max_temp)
