# Space Dogs Mission Control API

## Description
API for space mission simulation integrating external APIs. This project is developed during Global Hack Week: API to simulate mission control systems using real-world data sources.

## Planned Endpoints

- /status → Check API health
- /weather/launch-risk → Evaluate launch risk using weather data
- /telemetry → Simulated spacecraft telemetry data

## Tech Stack

- Python
- Flask
- REST APIs

## Status

In development (Day 1)
## API Functionality

### /weather/launch-risk

This endpoint evaluates launch risk using real-time weather data from an external API.

It considers:
- Temperature
- Wind speed

Based on these values, it classifies risk as:
- Low
- Medium
- High