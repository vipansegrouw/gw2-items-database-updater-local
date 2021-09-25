from google.cloud import bigquery


class BigQuery():
    def client(self):
        return bigquery.client.Client(project = "gw2-investment-management")

    def get_current_ids(self):
        sql = """SELECT id FROM `gw2-investment-tracker.gw2_items.gw2_items`"""
        return self.client().query(sql).result()
