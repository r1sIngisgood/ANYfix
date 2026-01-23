from pydantic import BaseModel
from typing import Optional

class ChangeCredentialsInputBody(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class TelegramAuthInputBody(BaseModel):
    enabled: bool

class TelegramAuthResponse(BaseModel):
    enabled: bool

class ChangeRootPathInputBody(BaseModel):
    root_path: Optional[str] = None
    action: str

class ChangeDomainPortInputBody(BaseModel):
    domain: Optional[str] = None
    port: Optional[int] = None
