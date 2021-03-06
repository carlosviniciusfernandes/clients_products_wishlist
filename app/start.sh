pip install virtualenv
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload --host '0.0.0.0' --port 8000