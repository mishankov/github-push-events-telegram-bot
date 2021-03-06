# GitHub push events Telegram bot

[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/mishankov/github-push-events-telegram-bot/actions?query=workflow%3Ablack)
[![CodeFactor](https://www.codefactor.io/repository/github/mishankov/github-push-events-telegram-bot/badge/main)](https://www.codefactor.io/repository/github/mishankov/github-push-events-telegram-bot/overview/main)

Receive `push` events from GitHub repository in Telegram bot

## Installation

Run `make install` for installation. If you don't have `make` installed, run commands from `install` action in `Makefile`

## Configuration

This application has some required and optional environment variables to set

### Required environment variables

- `TELEGRAM_BOT_TOKEN` - token of Telegram bot. [Documentation for Telegram bots](https://core.telegram.org/bots)
- `TELEGRAM_CHAT_ID` - chat id to send messages to. Get it from [`@my_id_bot`](https://t.me/my_id_bot) in Telegram for example

### Optional environment variables

- `GITHUB_WEBHOOK_SECRET` - secret part of your webhook URL. Default is `secret`
- `FASTAPI_OPENAPI_URL` - path to OpenAPI schema. More about that in [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/metadata/). Empty by default

## Run application localy

Run `make run` to run application an your local machine. If you don't have `make` installed, run commands from `run` action in `Makefile`

## Run application on a server

To run application on a server you probably want to run something like this

```bash
gunicorn --chdir src main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

This whould run you application in port `8000`. More about that in [Gunicorn documentation](https://docs.gunicorn.org/en/stable/configure.html)

## Run with Docker

To run this application with docker use `docker run` command similar to this

```bash
docker run -p 8000:8000 -e TELEGRAM_BOT_TOKEN=<TELEGRAM_BOT_TOKEN> -e TELEGRAM_CHAT_ID=<TELEGRAM_CHAT_ID> -d mishankov/github-push-events-telegram-bot:latest
```

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Cofigure GitHub webhook

Configure GitHub repository to send events about push events to `/github/repository/webhook/{GITHUB_WEBHOOK_SECRET}/` path on your server. More about that in [GitHub webhooks documentation](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)
 
