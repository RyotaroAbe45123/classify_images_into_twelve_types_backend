FROM python:3.10-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./api ./api
COPY ./start.sh ./start.sh
RUN chmod +x /start.sh

RUN apt -y update && apt -y upgrade && apt -y install libopencv-dev
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

CMD ["./start.sh"]
