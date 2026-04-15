

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

## 🔧 Backend Development — Submission Support

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

# 🚀 Space Dogs Mission Control API — Refactor Documentation (Day 4)

### Overview  
Today we took a big step forward in cleaning up the backend of our **Space Dogs Mission Control API**. The main goal of Day 4 was to **remove duplicated code**, improve the overall structure, and prepare the system for future features — especially the upcoming **AI integration**.

---

### The Problem We Faced  
Before the refactor, two important endpoints were doing almost the exact same work:

- `/weather/launch-risk`  
- `/launch-decision`

Both were independently:
- Calling the OpenWeather API  
- Parsing the response  
- Handling errors  

This created unnecessary duplication and made the code harder to maintain.

### Risks of the Old Approach  
- **Code duplication** → Same logic repeated in multiple places  
- **Inconsistent error handling** → Different behavior between endpoints  
- **Poor scalability** → Every change had to be made in several files  
- **Limited extensibility** → Adding new features (like AI) would mean copying the same code again  

---

### Our Solution  
We **centralized** all weather-related logic into a single, clean, reusable internal function:

```python
def get_weather_data(city):
```

This function now acts as a smart **abstraction layer** between our API endpoints and the external OpenWeather service.

---

### Key Improvements Made

#### 1. Fixed a Critical Bug  
We corrected this incorrect line:

```python
# Before (wrong)
API_KEY = "os.getenv("OPENWEATHER_KEY")"

# After (correct)
API_KEY = os.getenv("OPENWEATHER_KEY")
```

Now the API key is properly loaded from environment variables.

#### 2. New Centralized Function  
Here's the new `get_weather_data()` function:

```python
def get_weather_data(city):
    if not API_KEY:
        return None, {"error": "API key not configured"}
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
   
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        return None, {"error": "Request failed", "details": str(e)}
    
    if response.status_code != 200 or "main" not in data:
        return None, {"error": "Failed to fetch weather data", "details": data}
    
    return data, None
```

**Behavior**:  
- Returns `(data, None)` → when successful  
- Returns `(None, error)` → when something goes wrong  

---

### Updated Endpoints  
Both endpoints now use the new centralized function:

#### `/weather/launch-risk`
```python
data, error = get_weather_data(city)
if error:
    return jsonify(error), 500
```
Then it calculates temperature, wind speed, and launch risk level.

#### `/launch-decision`
```python
{data, error = get_weather_data(city)
if error:
    return jsonify(error), 500}
```
Then it returns a clear **GO / NO GO** decision based on wind conditions.

---

### Architectural Improvement  

**Before:**
```
Endpoint → OpenWeather API
Endpoint → OpenWeather API
```

**After:**
```
Endpoint → get_weather_data() → OpenWeather API
Endpoint → get_weather_data() → OpenWeather API
```

Much cleaner, right? ✨

---

### Benefits Achieved  

✅ **Better Maintainability** — Weather logic lives in one place only  
✅ **Consistent Behavior** — Same error handling and data format everywhere  
✅ **Improved Scalability** — Ready for AI, telemetry, caching, and more  
✅ **Less Redundancy** — No more duplicated API call code  

---

### Validation  
We tested everything thoroughly:

- Valid request: `/weather/launch-risk?city=Panama`  
- Decision endpoint: `/launch-decision?city=Panama`  
- Error handling: `/weather/launch-risk?city=InvalidCity123`  

All endpoints now return consistent and reliable results.

---

### Commit  
```bash
git commit -m "refactor: centralize weather API logic"
```

---

### Notes for Next Steps (Maryfer) 💡  

This version is now **stable and solid**. It’s ready for:  
- Updating the README documentation  
- Taking screenshots for the final submission  
- Building the new **AI endpoint** (`/ai/mission-advice`) on top of it  

> **Important**: This structure is our new **stable baseline**.  
> All future weather-related features **must** use `get_weather_data()` — never call `requests.get()` directly again.

---

### Final Thought  
This refactor turns our API from a messy, duplicated system into a clean, professional, and extensible architecture. It’s an essential foundation that will make adding AI and other exciting features much smoother during the rest of the hackathon.

We’re building something great — step by step! 🚀

---
🚀 Submission 1 — Telemetry
“Build a useless hack”

imagen 


When José finishes implementing the /telemetry/simulated endpoint, Maryfer takes over and does the following:
🎯 What to do:
Open your browser and visit:
texthttp://127.0.0.1:5000/telemetry/simulated

✨ What is this endpoint?
The /telemetry/simulated endpoint is a fun, simulated telemetry service for our Space Dogs mission.
Every time you refresh the page or make a new request, it generates completely random values for:

Altitude (in kilometers)
Velocity (in km/h)
Spacecraft Status

These values change dynamically with every request to simulate the ever-changing conditions of a real spaceflight.

⚠️ Important Note
The data shown is entirely fictional and randomly generated.
It does not represent real spacecraft telemetry.
Its only purpose is demonstration, testing, and pure hackathon fun!

Why is this “useless hack” awesome?
Because sometimes the best way to learn is by building something playful and pointless — just to see it work!
This endpoint brings the spirit of Global Hack Week to life: quick, visual, and instantly satisfying. Every refresh feels like checking in on a spaceship flying through the cosmos.
---
![6](https://github.com/user-attachments/assets/6029742b-1825-4f76-a941-4236dcf97d4a)


**Ready for launch!** 🌠

This API is built to be simple, reliable, and fun — exactly what a great hackathon project needs.

Would you like me to add emojis throughout, make it shorter, or include a "How to Run" section? Just let me know!
