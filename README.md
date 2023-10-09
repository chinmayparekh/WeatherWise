# WeatherWise - Temperature Alert System

## Description
The Temperature Alert Agent is a Python application built using the Fetch.ai uAgents library.
It connects to a free weather API to fetch real-time temperatures for a specified location and allows users to set their preferred temperature range. 
When the current temperature in the chosen location falls below the minimum or exceeds the maximum threshold, the agent sends an alert/notification to the user.

## Instructions to Run the Project

### Prerequisites
Before running the project, ensure you have the following prerequisites installed:

1. Python 3.7 or higher
2. The Fetch.ai uAgents library
3. An API key from OpenWeather (for weather data retrieval)

### Setup
1. Clone the repository:- 
=> git clone https://github.com/chinmayparekh/WeatherWise.git
=> cd WeatherWise

2. Activate virtual environment - poetry or pipenv

3. Open the `src/agents/temp.py` file and replace `api_key` with your OpenWeather API key.

4. Open the `src/agents/openweather.py` file and replace `api_key` with your OpenWeather API key.

### Running the Agent
1. Run the main.py script which is inside src directory.
2. Open new terminal window, then run temp_client.py which is inside src directory and follow the on-screen instructions to set your preferred temperature range and location.
3. Once configured, the agent will continuously monitor the temperature and send alerts according to given inputs.

## Special Considerations
- Ensure that you have an active internet connection for the agent to fetch real-time weather data.
- Make sure your OpenWeather API key is kept secure and not shared publicly.

Feel free to reach out for any questions or assistance!

