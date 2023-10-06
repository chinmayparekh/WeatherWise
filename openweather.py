import requests
import json

# API Key for OpenWeatherMap (Sign up for a free API key at https://openweathermap.org/api)
API_KEY = '9b255381736c9ac0f0ed5e708f213711'

# Function to fetch real-time weather data
def get_weather_data(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

# Function to check temperature against user preferences and send alerts
def check_temperature(city_name, min_temp, max_temp):
    weather_data = get_weather_data(city_name)

    if weather_data:
        temperature = weather_data['main']['temp']
        print(f"Current temperature in {city_name}: {temperature}°C")

        if temperature < min_temp:
            print(f"Alert: Temperature is below {min_temp}°C")
        elif temperature > max_temp:
            print(f"Alert: Temperature is above {max_temp}°C")
        else:
            print("Temperature is within the preferred range.")
    else:
        print("Unable to check temperature. Please try again later.")

if __name__ == "__main__":
    city_name = input("Enter the name of your preferred location: ")
    min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
    max_temp = float(input("Enter the maximum temperature threshold (in °C): "))
    check_temperature(city_name, min_temp, max_temp)
    # while True:
    #     check_temperature(city_name, min_temp, max_temp)
