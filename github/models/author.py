from typing import Optional

from pydantic import BaseModel


class Author(BaseModel):
    name: Optional[str]
    email: Optional[str]
