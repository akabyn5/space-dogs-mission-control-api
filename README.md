

# 🚀 Space Dogs Mission Control API

**A space mission simulation API that integrates real-world weather data to assess rocket launch risk.**

Built during **MLH Global Hack Week: APIs** — April 10–16, 2026.
---
![1](https://github.com/user-attachments/assets/d5d1f940-f102-456a-ae95-436801f7040b)


## ✨ Project Description

Space Dogs is a fun and educational API designed to simulate mission control systems. It connects to external weather APIs to provide real-time data and determine whether conditions are safe for a rocket launch.

Perfect for learning API integration, Flask development, and real-world data consumption in a space-themed project.

---

## 🛰️ Available Endpoints

### `GET /status`
Returns the basic health status of the API.

### `GET /weather/launch-risk?city=Panama`
The main endpoint. Fetches live weather data and evaluates launch risk.

**Returns:**
- `city`
- `temperature` (°C)
- `wind_speed` (m/s)
- `launch_risk` → `low` | `medium` | `high`

**Example Response:**
```json
{
  "city": "Panama",
  "temperature": 29,
  "wind_speed": 14,
  "launch_risk": "medium"
}
```

<img width="1024" height="627" alt="2" src="https://github.com/user-attachments/assets/707ab646-99b2-4bac-9997-0268e2ada24e" />

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **RESTful APIs**
- External integration with OpenWeather API

---
![3](https://github.com/user-attachments/assets/a4ecafd0-b243-430e-8a8d-b079f650e285)

![4](https://github.com/user-attachments/assets/c8b5697b-9712-4d9e-adb4-d45eebf9bbe8)

## 📅 Project Status

**In Development** — Day 1 of MLH Global Hack Week: APIs

---

## 🎯 How the Core Endpoint Works

The `/weather/launch-risk` endpoint pulls real-time weather information (temperature and wind speed) from an external API and intelligently classifies the **launch risk** as:

- **Low** — Safe conditions
- **Medium** — Caution advised
- **High** — Unsafe for launch


<img width="1200" height="675" alt="5" src="https://github.com/user-attachments/assets/d7a53ad4-b31f-42fc-b0f9-99ee64fbd7bb" />



This creates a realistic simulation of what real mission control teams evaluate before approving a launch.

---

## 🌌 About the Event

### MLH Global Hack Week: APIs (April 10–16, 2026)

A week-long virtual event by **Major League Hacking (MLH)** where participants learn by building.

Every day brings new challenges focused on APIs, GitHub, documentation, and project development. You submit your progress daily to earn points, badges, and community recognition.

**Space Dogs** is my contribution to this year’s API track — combining space exploration with practical API skills.

---

## 🔧 Backend Development — Block 3: Submission Support

**Date:** April 12, 2026  
**Responsible:** Backend (José)

### Objective
Transform the functional API into a stable, reusable component ready for multiple submissions without introducing instability.

### Goal of this Block
- Consolidate existing endpoints
- Ensure consistent and reliable responses
- Make the API easy to consume by other projects or submissions
- Keep changes minimal and low-risk

### Success Criteria
By the end of this block, the API will be:
- Stable and fully demonstrable
- Equipped with at least 3 functional endpoints
- Ready to be reused across different submissions
- Capable of being reinterpreted in various contexts

### Final Evaluation
The backend is considered successful when we can confidently say:

- “The API works with real data”
- “It can be queried by any city”
- “It consistently delivers launch risk assessment”
- “It can be reused in multiple scenarios without further changes”

---
![6](https://github.com/user-attachments/assets/6029742b-1825-4f76-a941-4236dcf97d4a)


**Ready for launch!** 🌠

This API is built to be simple, reliable, and fun — exactly what a great hackathon project needs.

Would you like me to add emojis throughout, make it shorter, or include a "How to Run" section? Just let me know!
