from typing import Optional, List

from pydantic import BaseModel

from github.models.commit import Commit
from github.models.author import Author
from github.models.repository import Repository
from github.models.user import User


class PushWebhookPayload(BaseModel):
    ref: Optional[str]
    before: Optional[str]
    after: Optional[str]
    commits: Optional[List[Commit]]
    pusher: Optional[Author]
    repository: Optional[Repository]
    sender: Optional[User]
