from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import random
import json
import os

app = FastAPI(title="Job Encouragement API")

# Load encouragement data
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
with open(DATA_FILE, "r") as f:
    ENCOURAGEMENTS = json.load(f)

# Allow CORS (open for dev, tighten later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # open during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static frontend
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

@app.get("/")
def root():
    """Serve frontend index page."""
    return {"message": "Visit /static/index.html to use the web UI."}

@app.get("/encouragement")
def get_general_encouragement():
    """Return a random piece of general encouragement."""
    return {"encouragement": random.choice(ENCOURAGEMENTS["general"])}

@app.get("/encouragement/{city}")
def get_city_encouragement(city: str):
    """Return encouragement for a specific city, or fallback to general."""
    city = city.lower().replace(" ", "_")
    if city in ENCOURAGEMENTS:
        return {"encouragement": random.choice(ENCOURAGEMENTS[city])}
    return {"encouragement": random.choice(ENCOURAGEMENTS["general"])}
