FROM python:3.8.5-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "watch_next.py"]