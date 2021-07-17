import requests
import pandas as pd
from sqlalchemy import create_engine

from config.connection_details import URI

BASE_URL = "https://rickandmortyapi.com/api"
CHARACTERS_TYPE = "character"
LOCATIONS_TYPE = f"location"
EPISODE_TYPE = f"episode"

ALL_TYPES = [CHARACTERS_TYPE, LOCATIONS_TYPE, EPISODE_TYPE]


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


def create_characters_to_episodes(engine, full_characters):
    ch_ep_df = full_characters[['id', 'episode']]
    ch_ep_df = ch_ep_df.explode('episode')
    ch_ep_df['episode'] = ch_ep_df['episode'].apply(url_to_id)
    ch_ep_df = ch_ep_df.rename(columns={'episode': 'episode_id', 'id': 'character_id'})
    print(ch_ep_df)
    ch_ep_df.to_sql('characters_in_episodes', schema='storefirst', con=engine, if_exists='append', index=False)


def characters_etl(engine):
    characters_fetcher = Fetcher(CHARACTERS_TYPE)
    full_characters = characters_fetcher.query_to_pandas([{'status': 'alive'}, {'status': 'dead'}])
    # create_characters_table(engine, full_characters)
    return full_characters


def create_characters_table(engine, full_characters):
    characters_df = full_characters[['id', 'name', 'species', 'type', 'gender', 'origin']]
    characters_df = characters_df.apply(characters_transform, axis=1, result_type='expand')
    characters_df = characters_df.rename(columns={'id': 'character_id', 'name': 'full_name'})
    characters_df.to_sql('characters', schema='storefirst', con=engine, if_exists='append', index=False)


def characters_transform(row):
    split_names(row)
    row['id'] = str(row['id'])
    row['origin'] = url_to_id(row['origin'].get('url'))
    return row


def split_names(row):
    splited_name = row['name'].split()
    if len(splited_name) == 2:
        row['first_name'] = splited_name[0]
        row['last_name'] = splited_name[1]
    else:
        row['first_name'] = None
        row['last_name'] = None

def url_to_id(url):
    return url.split('/')[-1]

def main():
    engine = create_engine(URI)
    full_characters_df = characters_etl(engine)
    episodes_etl(engine)


if __name__ == '__main__':
    main()
