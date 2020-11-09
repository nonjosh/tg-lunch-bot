FROM python:3.8-slim-buster

ENV TZ=Asia/Hong_Kong

COPY app/requirements.txt /app/



RUN apt-get update
RUN pip install -r /app/requirements.txt
RUN apt-get install -y net-tools


COPY app /app
WORKDIR /app

CMD ["python", "-u", "main.py"]