from typing import Optional, List

from pydantic import BaseModel

from models.commit import Commit
from models.author import Author
from models.repository import Repository
from models.user import User


class PushWebhookPayload(BaseModel):
    ref: Optional[str]
    before: Optional[str]
    after: Optional[str]
    commits: Optional[List[Commit]]
    pusher: Optional[Author]
    repository: Optional[Repository]
    sender: Optional[User]
