from typing import IO, Tuple, Dict

from yamldown import yamldown

def load(stream: IO[str]) -> Tuple[Dict, str]:
    return yamldown._load(stream)

def dump(yml: Dict, md: str, yamlfirst=True) -> str:
    return yamldown._dump(yml, md, yamlfirst=yamlfirst)
