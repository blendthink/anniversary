from datetime import date

from pydantic.dataclasses import dataclass


@dataclass
class Anniversary:
    key: str
    name: str
    date: date
