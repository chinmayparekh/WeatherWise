from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from .openweather import WeatherChecker
from messages.general import UAgentResponse, UAgentResponseType, KeyValue
from messages.temperature import Temperature
from dotenv import load_dotenv


import os
import uuid


TEMP_SEED = os.getenv("TEMP_SEED", "temp really secret phrase :)")

agent = Agent(
    name="temp_adaptor",
    seed=TEMP_SEED
)

fund_agent_if_low(agent.wallet.address())



temp_protocol = Protocol("temperature")

@temp_protocol.on_message(model=Temperature, replies={UAgentResponse})
async def temp_inferrence(ctx: Context, sender: str, msg: Temperature):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")

    location = msg.location
    max_temp = msg.max_temp
    min_temp = msg.min_temp

    try:
        load_dotenv()
        api_key = os.getenv('API_KEY')
        weather_checker = WeatherChecker(api_key)

        res = weather_checker.check_temperature(location, min_temp, max_temp)

        request_id = str(uuid.uuid4())
        options = []

        options.append(KeyValue(key="res", value = res))
        
        await ctx.send(sender, UAgentResponse(options=options, type=UAgentResponseType.SELECT_FROM_OPTIONS, request_id=request_id))
    except Exception as exc:
         ctx.logger.error(exc)
         await ctx.send(sender, UAgentResponse(message=str(exc), type=UAgentResponseType.ERROR))

agent.include(temp_protocol)