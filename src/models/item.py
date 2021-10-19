from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    type: str
    rarity: str


