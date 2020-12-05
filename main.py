import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.push_webhook_payload import PushWebhookPayload
from telegram_bot.bot import Bot


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID", "")

if TELEGRAM_BOT_TOKEN == "":
    raise Exception("TELEGRAM_BOT_TOKEN environmental variable is not set")
else:
    bot = Bot(TELEGRAM_BOT_TOKEN)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/github/repository/webhook/")
def receive_github_repository_webhook(payload: PushWebhookPayload):
    print([payload.__dict__])

    bot.send_message(chat_id=TELEGRAM_USER_ID, text="Push from: {}".format(payload.pusher.name))

    return {"status": "OK"}


@app.get("/")
def health_check():
    return {"status": "OK"}
