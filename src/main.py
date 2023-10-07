from uagents import Bureau

from agents.temp.temp import agent as temps_agent


if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)

    print(f"Adding temp agent to Bureau: {temps_agent.address}")
    bureau.add(temps_agent)
    bureau.run()

