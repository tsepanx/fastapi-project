# FastAPI project

A simple project template in Python using framework `FastAPI`.

Endpoints available:
- `/api/item` (CRUD)

### Setup

```bash
cp prod.env .env
```
And edit environment variables accordingly.

### Run

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

# OR

poetry install

# ---

cd backend

PYTHONPATH="./app" uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
# OR
PYTHONPATH="." python app/main.py
```

### Docker

#### Build image

```bash
cd backend
docker build -t fastapi-test .
```

#### Run with docker-compose

You may firstly edit `docker-compose.yml` before run:

from the project root dir:
```bash
docker-compose up
```
