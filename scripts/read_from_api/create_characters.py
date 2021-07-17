from config import CHARACTERS_TYPE
from scripts.read_from_api.Fetcher import Fetcher
from scripts.read_from_api.utils import url_to_id


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


def _create_characters_table(engine, full_characters):
    characters_df = full_characters[['id', 'name', 'species', 'type', 'gender', 'origin']]
    characters_df = characters_df.apply(_characters_transform, axis=1, result_type='expand')
    characters_df = characters_df.rename(columns={'id': 'character_id', 'name': 'full_name'})
    characters_df.to_sql('characters', schema='storefirst', con=engine, if_exists='append', index=False)


def _characters_transform(row):
    _split_names(row)
    row['id'] = str(row['id'])
    row['origin'] = url_to_id(row['origin'].get('url'))
    return row


def _split_names(row):
    splited_name = row['name'].split()
    if len(splited_name) == 2:
        row['first_name'] = splited_name[0]
        row['last_name'] = splited_name[1]
    else:
        row['first_name'] = None
        row['last_name'] = None