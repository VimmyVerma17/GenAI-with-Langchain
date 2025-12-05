import requests
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent

load_dotenv()

# Tools
search_tool = DuckDuckGoSearchRun()

@tool(description="Get the current weather for a city")
def get_weather_data(city: str) -> str:
    url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'
    response = requests.get(url).json()
    if "current" not in response:
        return f"Could not fetch weather for {city}"
    temp = response["current"]["temperature"]
    desc = response["current"]["weather_descriptions"][0]
    return f"Weather in {city}: {temp}°C, {desc}"

tools = [search_tool, get_weather_data]

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.4)

# Creating Agent
agent = create_agent(
    llm,
    tools,
    system_prompt="You are a helpful assistant that can use search and weather tools."
)

# Running Agent 
query = "Find the capital of Madhya Pradesh and then check its current weather"
response = agent.invoke({"messages": [{"role": "user", "content": query}]})

# Cleaning Output
print("\nFINAL OUTPUT:\n")

if isinstance(response, dict) and "messages" in response:
    final_message = response["messages"][-1]  # last AI message
    print(final_message.content)
else:
    print(response)
