# Import the Bureau class from the uagents module
from uagents import Bureau

# Import the temp agent instance from another module
from agents.temp.temp import agent as temps_agent

if __name__ == "__main__":
    # Create a Bureau instance with a specified endpoint and port
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)

    # Print a message indicating the addition of the temp agent to the Bureau
    print(f"Adding temp agent to Bureau: {temps_agent.address}")

    # Add the temp agent to the Bureau
    bureau.add(temps_agent)

    # Start running the Bureau
    bureau.run()
