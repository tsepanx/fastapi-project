# FastAPI project


### Run

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
# OR
poetry install
# ---
PYTHONPATH="$PWD/backend" uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```