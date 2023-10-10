# Import necessary modules and classes
import sys
from messages.temperature import Temperature
from messages.general import UAgentResponse
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os

# Load the TEMP_SEED from environment variables with a default value
TEMP_SEED = os.getenv("TEMPERATURE_SEED", "top_destinations_client really secret phrase :)")

# Create an Agent instance for the temperature client
temp_client = Agent(
    name="temp_client",
    port=8008,
    seed=TEMP_SEED,
    endpoint=["http://127.0.0.1:8008/submit"],  # Define the endpoint for sending messages
)

# Fund the agent's wallet if it's low on funds
fund_agent_if_low(temp_client.wallet.address())

# Prompt the user for input
city_name = input("Enter the name of your preferred location: ")
min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
max_temp = float(input("Enter the maximum temperature threshold (in °C): "))

# Create a Temperature message with user input
temp_request = Temperature(location=city_name, max_temp=max_temp, min_temp=min_temp)


# Define a message sender function on an interval
@temp_client.on_interval(period=100.0)  # Send a message every 100 seconds
async def send_message(ctx: Context):
    # Send the Temperature request to a specific agent
    await ctx.send("agent1qwrkwmd86qym8k4e4kh9sr3urgyqpfvra04jugjsr252zwmemsehy4vwtdz", temp_request)


# Define a message handler for UAgentResponse messages
@temp_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"Received top destination options from: {msg.options}")


# Start the client agent
if __name__ == "__main__":
    temp_client.run()
