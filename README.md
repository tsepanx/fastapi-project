# FastAPI project


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
PYTHONPATH="." python app/main.py
```
