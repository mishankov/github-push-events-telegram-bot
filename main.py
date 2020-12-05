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

    message = "New push in repository [{}]({})".format(
        payload.repository.full_name, payload.repository.html_url
    )
    if payload.sender is not None:
        message += " from [{}]({})".format(
            payload.sender.login, payload.sender.html_url
        )

    if len(payload.commits) > 0:
        message += "\n *Commits:*"
        for commit in payload.commits:
            message += "\n- _[{}]({})_".format(commit.id, commit.url)
            message += "\n Message: {}".format(commit.message)

            if len(commit.added) > 0:
                message += "\n  _Added:_ {}".format(",".join(commit.added))

            if len(commit.removed) > 0:
                message += "\n  Removed:_ {}".format(",".join(commit.removed))

            if len(commit.modified) > 0:
                message += "\n  _Modified:_ {}".format(",".join(commit.modified))

    bot.send_message(chat_id=TELEGRAM_USER_ID, parse_mode="MarkdownV2", text=message)

    return {"status": "OK"}


@app.get("/")
def health_check():
    return {"status": "OK"}
