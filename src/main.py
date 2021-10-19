from src.clients.gw2client import GW2Client
from src.utils import write_items, get_current_item_ids, get_new_item_ids


def main():
    gw2_client = GW2Client()
    item_ids = gw2_client.get_items()
    #  todo these need to be ids not items
    items = gw2_client.get_items(item_ids)
    #  todo write all items to file - it's json so you can't just do the new ones
    write_items(items_all)


if __name__ == "__main__":
    main()
