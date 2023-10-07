import sys

from messages.temperature import Temperature
from messages.general import UAgentResponse
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os

TEMP_SEED = os.getenv("TEMPERATURE_SEED", "top_destinations_client really secret phrase :)")
temp_client = Agent(
    name="temp_client",
    port=8008,
    seed=TEMP_SEED,
    endpoint=["http://127.0.0.1:8008/submit"],
)
fund_agent_if_low(temp_client.wallet.address())

city_name = input("Enter the name of your preferred location: ")
min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
max_temp = float(input("Enter the maximum temperature threshold (in °C): "))

temp_request = Temperature(location=city_name,max_temp=max_temp,min_temp=min_temp)

@temp_client.on_interval(period=100.0)
async def send_message(ctx: Context):
    await ctx.send("agent1qwrkwmd86qym8k4e4kh9sr3urgyqpfvra04jugjsr252zwmemsehy4vwtdz", temp_request)

@temp_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"Received top destination options from: {msg.options}")
    
if __name__ == "__main__":
    temp_client.run()