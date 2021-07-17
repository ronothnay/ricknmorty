from config import EPISODE_TYPE
from scripts.read_from_api.Fetcher import Fetcher


def episodes_etl(engine):
    characters_fetcher = Fetcher(EPISODE_TYPE)
    full_episodes = characters_fetcher.query_to_pandas()
    full_episodes = full_episodes[['id', 'name', 'air_date', 'episode']]
    full_episodes['season_id'] = full_episodes['episode'].str.extract(r'S0?(\d+).*', expand=False)
    full_episodes = full_episodes.rename(columns={'id': 'episode_id', 'episode': 'episode_code'})
    full_episodes.to_sql('episodes', schema='storefirst', con=engine, if_exists='append', index=False)
