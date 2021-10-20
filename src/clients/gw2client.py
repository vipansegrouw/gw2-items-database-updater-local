from typing import List, Any

from gw2api import GuildWars2Client

from src.models.item import Item


class GW2Client:
    def gw2_client(self):
        return GuildWars2Client()

    def get_items_or_ids_from_api(self, ids: List[int] = None):
        return self.gw2_client().items.get(ids=ids)

    def get_items(self, ids: List[int] = None) -> List[Item]:
        items = []
        items_objects = []
        ids_batch = []
        while ids:
            while len(ids_batch) < 200 and ids:
                ids_batch.append(ids.pop())
            item_batch = self.get_items_or_ids_from_api(ids_batch)
            items.extend(item_batch)
            print(ids_batch)
            ids_batch = []
        for item in items:
            new_item = Item(item['id'], item['name'], item['type'], item['rarity'])
            items_objects.append(new_item)
        return items_objects
