# JobLift

A simple FastAPI microservice that provides encouragement and perspective for job seekers.
Users can receive random encouragement or select a U.S. city for localized advice.

The app serves both:

* **REST API endpoints** for programmatic access
* **Static frontend UI** (HTML/JS) bundled inside the FastAPI app

Deployed easily with Docker or on free cloud tiers like Render.

---

## ✨ Features

* **Encouragement API**

  * `GET /encouragement` → random general encouragement
  * `GET /encouragement/{city}` → random encouragement for that city, or fallback to general

* **Frontend**

  * Simple dropdown of 20 major U.S. cities
  * “Give me advice” button fetches encouragement from the API

* **Extras**

  * CORS enabled (open during development, lock down later)
  * Lightweight `data.json` with encouragement quotes
  * Unit tests with `pytest`
  * Dockerized for easy deployment

---

## 📂 Project Structure

```
joblift/
│
├── app/
│   ├── __init.py__          # empty file (has use for test environment config "tagging" for app, see below)
│   ├── data.json            # Encouragement data
│   ├── main.py              # FastAPI app & endpoints
│   ├── static/              # Frontend files
│   │   ├── index.html
│   │   └── script.js
│   └── tests/
│       └── conftest.py      # Unit test setup (specific to any environment issues detecting app as a "package")
│       └── test_api.py      # Unit tests
│

├── .dockerignore
├── .gitignore
├── Dockerfile               # Container build
├── Makefile                 # for Render hosting
├── README.md
├── render.yaml              # for Render "one-touch" build setup
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOURUSERNAME/joblift.git
cd joblift
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run locally

```bash
uvicorn app.main:app --reload
```

Visit:

* API root → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Frontend → [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

---

## 🧪 Running Tests

```bash
pytest app/tests
```

---

## 🐳 Docker Setup

### Build the image

```bash
docker build -t joblift .
```

### Run the container

```bash
docker run -p 8000:8000 joblift
```

Visit the app at:
[http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

---

## 🌐 Deployment

* **Render (recommended)**: Easiest free-tier hosting for FastAPI.
* **AWS / Azure**: Works via container services (ECS, App Service).

The Dockerfile is preconfigured, so just push and deploy.

---

## 🗂️ Example API Usage

### General Encouragement

```bash
curl http://127.0.0.1:8000/encouragement
```

Response:

```json
{"encouragement": "Keep pushing forward — rejection is redirection."}
```

### City Encouragement

```bash
curl http://127.0.0.1:8000/encouragement/chicago
```

Response:

```json
{"encouragement": "Chicago is a city of second chances. Keep your head high."}
```

---

## Existing Issues
* Text formatting produces some weird symbols
* This (like so many other projects) could use more testing

## 🔮 Future Ideas

* Expand dataset to include **all U.S. cities / states**
* Store data in a lightweight DB (SQLite, Postgres)
* Add support for **user-contributed encouragement**
* Deploy frontend separately (e.g. GitHub Pages) with API calls

---

🙏 Thanks for checking out **JobLift**.
If you’re a job seeker:
**You are not alone, and your next opportunity is on its way.**