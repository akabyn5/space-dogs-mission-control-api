## Space Dogs Mission Control API

API for space mission simulation that integrates weather APIs to assess launch risk.

## Description
API for space mission simulation integrating external APIs. This project is developed during Global Hack Week: API to simulate mission control systems using real-world data sources.

## Planned Endpoints
## Endpoints

### /status
Returns the basic status of the API

### /weather/launch-risk?city=Panama
Returns:
- temperature
- wind speed
- launch risk (low, medium, high)

  
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
- 
## Example Request

GET /weather/launch-risk?city=Panama


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


## Example Response

{
  "city": "Panama",
  "temperature": 29,
  "wind_speed": 14,
  "launch_risk": "medium"
}

SUBMISSION SUPPORT (API)**  
**Date:** April 12, 2026  
**Responsible:** Backend (José)  
**Objective:** Turn the functional API into a direct input for geneability.

---

### 1. BLOCK OBJECTIVE

The purpose of this block is **not** to develop complex new features, but to:

- Consolidate the existing endpoints as usable products
- Facilitate their consumption for submissions
- Clearly expose the API’s behavior
- (Optional) Add one low-risk additional endpoint to expand use cases

Any modification outside this scope introduces unnecessary risk.

---

### 2. REQUIRED CURRENT STATE OF THE API

Before proceeding, the API must meet the following conditions:

- `/status` endpoint operational
- `/status/detailed` endpoint operational
- `/weather/launch-risk` endpoint working with a real API
- Error handling implemented (no crashes)
- Use of environment variable for the API key (`OPENWEATHER_KEY`)

If any of these conditions are not met, do not proceed.

---

### 3. PREPARING THE API FOR SUBMISSIONS

The backend must deliver structured information for external consumption. This involves:

#### 3.1 Main Documented Endpoint

The key endpoint is:

`/weather/launch-risk?city=Panama`

It must guarantee:

- Consistent JSON response format
- Present fields:
  - `city`
  - `temperature`
  - `wind_speed`
  - `launch_risk`

#### 3.2 Error Behavior

It must respond correctly in the following cases:

- Invalid city → returns JSON with `"error"` and `"details"`
- Missing API key → `"API key not configured"`
- Network failure → `"Request failed"`

This is critical to avoid failures during demonstrations.

---

### 4. TECHNICAL DELIVERABLES FOR SUBMISSIONS

The backend must provide exactly the following elements:

#### 4.1 Functional Endpoint

Example request:

`/weather/launch-risk?city=Panama`

Example real response:

```json
{
  "city": "Panama",
  "temperature": 28.18,
  "wind_speed": 3.21,
  "launch_risk": "low"
}
```

#### 4.2 Technical Description of the Endpoint

Minimum definition:

> “This endpoint integrates the OpenWeather API to evaluate rocket launch risk based on real-time wind speed.”

#### 4.3 Additional Available Endpoints

- `/status`
- `/status/detailed`

These strengthen the perception of a complete system.

---

### 5. CONTROLLED EXTENSION (OPTIONAL)

Only if the API is completely stable, one additional endpoint may be added.

#### 5.1 Endpoint: `/launch-decision`

**Purpose:** Translate weather data into a binary decision.

**Implementation:**

```python
@app.route("/launch-decision")
def decision():
    city = request.args.get("city", "Panama")

    if not API_KEY:
        return jsonify({"error": "API key not configured"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        return jsonify({"error": "Failed to fetch weather data"}), 500

    wind = data["wind"]["speed"]

    if wind > 20:
        decision = "NO GO"
    else:
        decision = "GO"

    return jsonify({
        "city": city,
        "decision": decision
    })
```

#### 5.2 Technical Justification

- Reuses existing logic (does not introduce complexity)
- Enables new usage approaches:
  - Decision system
  - Simulator
  - Game logic

---

### 6. FINAL API VALIDATION

Before considering the block complete, the following tests must be executed:

- `/status`
- `/status/detailed`
- `/weather/launch-risk?city=Panama`
- `/weather/launch-risk?city=InvalidCity123`
- (Optional) `/launch-decision?city=Panama`

**Acceptance Criteria:**

- All routes respond
- No uncontrolled errors
- No unhandled exceptions on the server

---

### 7. CHANGE CONTROL (COMMITS)

Progress must be recorded with clear commits:

- `"feat: stabilize weather endpoint for submissions"`
- `"feat: add detailed status endpoint"`
- `"feat: add launch decision endpoint"` (if applicable)

This provides traceability and improves repository evaluation.

---

### 8. CRITICAL RESTRICTIONS

During this block, the following actions are **explicitly prohibited**:

- Restructuring the project
- Adding new dependencies
- Introducing a database
- Modifying the architecture
- Implementing multiple new endpoints

These actions do not provide immediate value and increase the risk of failure.

---

### 9. EXPECTED RESULT

Upon completion of this block, the API must:

- Be stable and demonstrable
- Have at least 3 functional endpoints
- Be ready to be reused in multiple submissions
- Allow reinterpretation of the same system in different contexts

---

### 10. FINAL EVALUATION

The backend is considered successful if it is possible to affirm:

- “The API works with real data”
- “It can be queried by city”
- “It delivers launch risk consistently”
- “It can be reused in multiple scenarios without additional changes”

---

**Ready to use for your GitHub repository or documentation.** Let me know if you need a version with emojis or a more compact format.
