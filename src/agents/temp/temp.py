# Import necessary modules and classes
from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from .openweather import WeatherChecker  # Import WeatherChecker from a local module
from messages.general import UAgentResponse, UAgentResponseType, KeyValue
from messages.temperature import Temperature
from dotenv import load_dotenv

import os
import uuid

# Load the TEMP_SEED from environment variables with a default value
TEMP_SEED = os.getenv("TEMP_SEED", "temp really secret phrase :)")

# Create an Agent instance with a name and seed
agent = Agent(
    name="temp_adaptor",
    seed=TEMP_SEED
)

# Fund the agent's wallet if it's low on funds
fund_agent_if_low(agent.wallet.address())

# Define a Protocol for handling temperature-related messages
temp_protocol = Protocol("temperature")


# Define a message handler for Temperature messages
@temp_protocol.on_message(model=Temperature, replies={UAgentResponse})
async def temp_inference(ctx: Context, sender: str, msg: Temperature):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")

    # Extract information from the Temperature message
    location = msg.location
    max_temp = msg.max_temp
    min_temp = msg.min_temp

    try:
        # Load API key from a .env file using dotenv
        load_dotenv()
        api_key = os.getenv('API_KEY')

        # Create an instance of the WeatherChecker class with the API key
        weather_checker = WeatherChecker(api_key)

        # Check the temperature using the WeatherChecker
        res = weather_checker.check_temperature(location, min_temp, max_temp)

        # Generate a unique request ID
        request_id = str(uuid.uuid4())
        options = []

        # Add the result to the options
        options.append(KeyValue(key="res", value=res))

        # Send a UAgentResponse message with the result
        await ctx.send(sender, UAgentResponse(options=options, type=UAgentResponseType.SELECT_FROM_OPTIONS,
                                              request_id=request_id))
    except Exception as exc:
        # Handle exceptions and send an error response
        ctx.logger.error(exc)
        await ctx.send(sender, UAgentResponse(message=str(exc), type=UAgentResponseType.ERROR))


# Include the temperature protocol in the agent
agent.include(temp_protocol)
