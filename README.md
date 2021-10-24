# FastAPI project


### Run

```bash
cd backend

virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

PYTHONPATH="$PWD/../" uvicorn main:app --reload --host 0.0.0.0 --port 8001
```
