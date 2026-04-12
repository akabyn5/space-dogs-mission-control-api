## Space Dogs Mission Control API

API para simulación de misiones espaciales que integra APIs de clima para evaluar el riesgo de lanzamiento.

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

- # MLH Global Hack Week: APIs — Summary

## Overview
**MLH Global Hack Week (GHW): APIs** is a week-long virtual event where developers, students, and tech enthusiasts learn and build projects using public APIs. It is organized by Major League Hacking (MLH) and runs from **April 10th to 16th, 2026**.

## How It Works
- Participants join online and complete **daily challenges**.
- Each challenge focuses on learning a specific skill (e.g., APIs, GitHub, project development).
- You submit your work through the platform to earn **points, badges, or recognition**.
- Submissions usually include:
  - Code (e.g., GitHub repository)
  - Screenshots or outputs
  - A short description of your project

## What It Consists Of
- **Hands-on learning:** Build real projects instead of just watching tutorials.
- **API integration:** Use public APIs to fetch and process real-world data.
- **Project submissions:** Share your work with the community.
- **Collaboration:** Optional teamwork or individual participation.
- **Mentorship & support:** Guidance from MLH mentors and community members.

## Example Project (From the Screenshot)
A sample submission shows:
- An API that evaluates **launch risk** based on weather data.
- Technologies used:
  - Python
  - Flask
  - JSON
  - GitHub Copilot
- 


# Backboard Challenge Summary

## What is Backboard?
Backboard is an all-in-one AI stack delivered through a single API. It provides:
- Memory
- AI models
- Assistants
- Document processing
- Persistent conversations

## Challenge Objective
Create your first AI assistant, start a conversation with it, and receive a response. The goal is to build a ChatGPT-like assistant controlled through code in just three steps.

## How It Works

### Step 1: Create an Assistant
An Assistant is an AI agent with custom instructions. You create one by defining:
- `name`: e.g., "My First Assistant"
- `system_prompt`: e.g., "You are a helpful assistant that responds concisely."

### Step 2: Create a Thread
A Thread represents a conversation session. You link it to your assistant to maintain context.

### Step 3: Send a Message (Non-Streaming)
Send a message (e.g., "Say Hello World") and get a complete response back. You can choose streaming or non-streaming mode.

## Key Features
- **Persistent Conversations** – Threads maintain context across multiple messages
- **Document Processing** – Upload and process PDFs, text, Office files
- **Memory** – Assistants remember facts and preferences across conversations
- **Tools & Custom Instructions** – Extend assistant capabilities

## Submission Requirement
Submit a link to your **GitHub Repository** with your implementation.

## Base API URL
