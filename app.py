from langgraph.graph import StateGraph, START, END

from typing import TypedDict

class TemparatureState(TypedDict):
    temperature: float
    farenheit: float
    weather_status: str

# Define and compile graph

def convert_to_farenheit(state: TemparatureState) -> TemparatureState:
    celsius = state["temperature"]
    # Convert Celsius to Fahrenheit
    farenheit = (celsius * 9/5) + 32
    state["farenheit"] = round(farenheit, 2)
    return state

def label_weather_status(state: TemparatureState) -> TemparatureState:
    farenheit = state["farenheit"]

    if farenheit < 50:
        state["weather_status"] = "Cold"
    elif 50 <= farenheit < 77:
        state["weather_status"] = "Mild"
    elif 77 <= farenheit < 95:
        state["weather_status"] = "Hot"
    elif 95 <= state["temperature"] < 107:
        state["weather_status"] = "Very Hot"
    else:
        state["weather_status"] = "Extremely Hot"
    return state

graph = StateGraph(TemparatureState)

# Add nodes and edges to the graph
graph.add_node("convert_temp", convert_to_farenheit)
graph.add_edge(START, "convert_temp")
graph.add_node("label_weather", label_weather_status)
graph.add_edge("convert_temp", "label_weather")
graph.add_edge("convert_temp", END) 

# Compile the graph to validate its structure and prepare it for execution
graph = graph.compile()

""" initial_state: TemparatureState = {"temperature": 28.5, "farenheit": 0.0} """
initial_state: TemparatureState = {"temperature": 25.0, "farenheit": 0.0, "weather_status": ""}
result = graph.invoke(initial_state)
print(result)  # Output: {'temperature': 25.0, 'farenheit': 77.0}

