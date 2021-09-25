from src.clients.bigquery import BigQuery
from src.clients.gw2client import GW2Client


def main():
    gw2_client = GW2Client()
    big_query_client = BigQuery()
    item_ids = [6, 15]
    items = gw2_client.get_items(item_ids)
    current_items = big_query_client.get_current_ids()
    print(current_items)


if __name__ == "__main__":
    main()
