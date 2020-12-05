from typing import Optional, List

from pydantic import BaseModel

from github.models.author import Author


class Commit(BaseModel):
    id: Optional[str]
    timestamp: Optional[str]
    message: Optional[str]
    author: Optional[Author]
    url: Optional[str]
    distinct: Optional[bool]
    added: Optional[List[str]]
    modified: Optional[List[str]]
    removed: Optional[List[str]]
