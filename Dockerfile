FROM python:3.10-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./api ./api

RUN apt -y update && apt -y upgrade && apt -y install libopencv-dev
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload", "--port", "${PORT:-5000"]
