from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Item:
    id: int
    name: str
    type: str
    rarity: str


