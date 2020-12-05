import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from github.models.push_webhook_payload import PushWebhookPayload
from telegram.bot import Bot
from telegram.utils import escape_html

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID", "")
GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "secret")

if TELEGRAM_BOT_TOKEN == "":
    raise Exception("TELEGRAM_BOT_TOKEN environmental variable is not set")
else:
    bot = Bot(TELEGRAM_BOT_TOKEN)

if TELEGRAM_USER_ID == "":
    raise Exception("TELEGRAM_USER_ID environmental variable is not set")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/github/repository/webhook/{}/".format(GITHUB_WEBHOOK_SECRET))
def receive_github_repository_webhook(payload: PushWebhookPayload):
    message = "New push in repository <a href='{}'>{}</a>".format(
        payload.repository.html_url, escape_html(payload.repository.full_name)
    )

    if payload.sender is not None:
        message += " from <a href='{}'>{}</a>".format(
            payload.sender.html_url, escape_html(payload.sender.login)
        )

    if len(payload.commits) > 0:
        message += "\n<b>Commits:</b>"
        for commit in payload.commits:
            message += "\n<a href='{}'>{}</a>".format(
                commit.url, escape_html(commit.id)
            )
            message += "\n  <i>Message:</i> {}".format(escape_html(commit.message))

            if len(commit.added) > 0:
                message += "\n  <i>Added:</i> {}".format(
                    escape_html(", ".join(commit.added))
                )

            if len(commit.removed) > 0:
                message += "\n  <i>Removed:</i> {}".format(
                    escape_html(", ".join(commit.removed))
                )

            if len(commit.modified) > 0:
                message += "\n  <i>Modified:</i> {}".format(
                    escape_html(", ".join(commit.modified))
                )

    bot.send_message(chat_id=TELEGRAM_USER_ID, parse_mode="HTML", text=message)

    return {"status": "OK"}


@app.get("/")
def health_check():
    return {"status": "OK"}
