FROM python:3.9-slim-buster AS builder
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends gcc make libc6-dev \
  && rm -rf /var/lib/apt/lists/* \
  && python3 -m venv venv \
  && . venv/bin/activate \
  && pip install --upgrade pip \
  && pip install -r requirements.txt


FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY src /app/src
CMD . venv/bin/activate ; gunicorn --chdir src main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
EXPOSE 8000
