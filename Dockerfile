FROM python:3.12-slim

WORKDIR /app
COPY . /app/

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]