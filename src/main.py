from src.clients.gw2client import GW2Client
from src.utils import write_items, get_current_item_ids, get_new_item_ids


def main():
    gw2_client = GW2Client()
    item_ids = gw2_client.get_items_or_ids_from_api()
    items = gw2_client.get_items(item_ids)
    write_items(items)


if __name__ == "__main__":
    main()
