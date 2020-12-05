import os
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

if TELEGRAM_BOT_TOKEN == "":
    raise Exception("TELEGRAM_BOT_TOKEN is not passed")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    login: str
    name: str
    email: str
    id: int
    html_url: str


class Repository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    html_url: str
    stargazers_count: int
    watchers_count: int
    language: str
    private: bool
    owner: User


class Author(BaseModel):
    name: str
    email: str


class Commit(BaseModel):
    id: str
    timestamp: str
    message: str
    author: Author
    url: str
    distinct: bool
    added: List[str]
    modified: List[str]
    removed: List[str]


class PushWebhookPayload(BaseModel):
    ref: str
    before: str
    after: str
    commits: List[Commit]
    pusher: Author
    repository: Repository
    sender: User


@app.post("/github/repository/webhooks/")
def receive_github_repository_webhook(payload: PushWebhookPayload):
    print([payload.__dict__])

    return {"status": "OK"}


@app.get("/")
def health_check():
    return {"status": "OK"}
