import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.push_webhook_payload import PushWebhookPayload
from telegram.bot import Bot

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

    message = "New push in repository <a href='{}'>{}</a>".format(
        payload.repository.html_url, payload.repository.full_name
    )

    if payload.sender is not None:
        message += " from <a href='{}'>{}</a>".format(
            payload.sender.html_url, payload.sender.login
        )

    if len(payload.commits) > 0:
        message += "\n<b>Commits:</b>"
        for commit in payload.commits:
            message += "\n<a href='{}'>{}</a>".format(commit.url, commit.id)
            message += "\n  <i>Message:</i> {}".format(commit.message)

            if len(commit.added) > 0:
                message += "\n  <i>Added:</i> {}".format(",".join(commit.added))

            if len(commit.removed) > 0:
                message += "\n  <i>Removed:</i> {}".format(",".join(commit.removed))

            if len(commit.modified) > 0:
                message += "\n  <i>Modified:</i> {}".format(",".join(commit.modified))

    bot.send_message(chat_id=TELEGRAM_USER_ID, parse_mode="HTML", text=message)

    return {"status": "OK"}


@app.get("/")
def health_check():
    return {"status": "OK"}
