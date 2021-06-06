from dataclasses import dataclass
from datetime import date


@dataclass
class Anniversary:
    key: str
    name: str
    date: date
