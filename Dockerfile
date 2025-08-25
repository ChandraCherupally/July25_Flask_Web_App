FROM python:3.12.2-slim

WORKDIR /flask-docker

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "--app", "loan_approval_predictor.py", "run", "--host=0.0.0.0", "--port=5000"]



