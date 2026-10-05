# LangGraph Temperature Demo

A small Python project demonstrating a stateful workflow with [LangGraph](https://langchain-ai.github.io/langgraph/). The graph takes a Celsius temperature, converts it to Fahrenheit, and assigns a weather-status label.

## Requirements

- Python
- Packages listed in `requirements.txt`

## Set up

From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python app.py
```

The example input is set in `app.py` (`25.0` °C). Change the `temperature` value in `initial_state` to try a different input.

## How it works

The graph passes a shared state through two nodes:

1. `convert_temp` converts the `temperature` value from Celsius to Fahrenheit and rounds it to two decimal places.
2. `label_weather` sets `weather_status` based on the converted temperature.

The state is defined by `TemparatureState` and contains:

- `temperature`: input temperature in Celsius
- `farenheit`: converted temperature in Fahrenheit
- `weather_status`: the assigned label