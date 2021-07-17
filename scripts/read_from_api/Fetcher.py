import requests
import pandas as pd

from config import ALL_TYPES, BASE_URL


class Fetcher:
    def __init__(self, object_type: str):
        if object_type not in ALL_TYPES:
            raise ValueError("An illegal object type was given")
        self.object_type = object_type
        self.url = f"{BASE_URL}/{object_type}"

    def query_to_pandas(self, list_of_queries: [dict] = None) -> pd.DataFrame:
        all_results = []
        if not list_of_queries:
            all_results.extend(self._fetch(self.url))
        else:
            for query in list_of_queries:
                query_url = "&".join([f"{param_name}={param_value}" for param_name, param_value in query.items()])
                final_url = f"{self.url}?{query_url}"
                all_results.extend(self._fetch(final_url))
        return pd.DataFrame(all_results)

    def _fetch(self, url: str) -> [dict]:
        all_results = []
        data = requests.get(url).json()
        all_results.extend(data['results'])
        while data['info'].get('next'):
            data = requests.get(data['info'].get('next')).json()
            all_results.extend(data['results'])
        return all_results
