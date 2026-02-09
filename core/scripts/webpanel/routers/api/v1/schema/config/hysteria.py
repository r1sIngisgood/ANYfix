from pydantic import BaseModel, RootModel
from typing import Any



class ConfigFile(RootModel):
    root: dict[str, Any]


class GetPortResponse(BaseModel):
    port: int


class GetSniResponse(BaseModel):
    sni: str

class GetObfsResponse(BaseModel):
    obfs: str
    
class GetMasqueradeStatusResponse(BaseModel):
    status: str

class PortHoppingStatusResponse(BaseModel):
    enabled: bool
    port_range: str
    server_port: str
    iptables_active: bool = False