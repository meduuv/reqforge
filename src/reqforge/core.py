from dataclasses import dataclass,field
from urllib.parse import urlencode

@dataclass
class RequestSpec:
    method:str="GET"; url:str=""; headers:dict[str,str]=field(default_factory=dict); params:dict[str,str]=field(default_factory=dict); body:str|None=None
    def build_url(self):
        if not self.url.startswith(("http://","https://")): raise ValueError("URL must use HTTP or HTTPS")
        return self.url + (("&" if "?" in self.url else "?")+urlencode(self.params) if self.params else "")
