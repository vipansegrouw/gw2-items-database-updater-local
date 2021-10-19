import json
from typing import List, Any, Dict

from src.models.item import Item


def write_items(items: List[Item]):
    with open("./resources/item_database.json", 'w') as file:
        items_dicts = item_objects_to_dicts(items)
        items_str = json.dumps(items_dicts, indent=2)
        file.write(items_str)
        file.close()


def item_objects_to_dicts(items: List[Item]) -> List[Dict[str, Any]]:
    return [item.__dict__ for item in items]


def json_line_to_item_object(json_str: str) -> Item:
    dict = json.loads(json_str)
    return Item(dict['id'], dict['name'], dict['type'], dict['rarity'])


def load_json_items():
    with open("./resources/item_database.json", 'r') as file:
        return json.load(file)


def get_current_item_ids() -> List[int]:
    items_dicts = load_json_items()
    return [item['id'] for item in items_dicts]


def get_new_item_ids(current_ids: List[int], item_ids: List[int]) -> List[int]:
    new_ids = []
    for id in item_ids:
        if id not in current_ids:
            new_ids.append(id)
    return new_ids
