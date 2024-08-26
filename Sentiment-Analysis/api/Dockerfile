FROM python:3.9-slim

WORKDIR /app

COPY api/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api/ .

CMD ["python", "app.py"]
