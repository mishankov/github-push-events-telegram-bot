from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    login: Optional[str]
    name: Optional[str]
    email: Optional[str]
    id: Optional[int]
    html_url: Optional[str]
