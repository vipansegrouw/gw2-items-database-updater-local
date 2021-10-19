from typing import List

from gw2api import GuildWars2Client

from src.models.item import Item


class GW2Client:
    def gw2_client(self):
        return GuildWars2Client()

    def get_list_of_all_item_ids(self) -> List[int]:
        return self.gw2_client().items.get()

    def get_items(self, ids: List[int] = None) -> List[Item]:

        #  todo this should batch in groups of 200

        items_list = self.gw2_client().items.get(ids=ids)
        items = []
        for item in items_list:
            new_item = Item(item['id'], item['name'], item['type'], item['rarity'])
            items.append(new_item)
        return items
