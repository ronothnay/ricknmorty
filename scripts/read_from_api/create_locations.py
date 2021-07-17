from config import LOCATIONS_TYPE
from scripts.read_from_api.Fetcher import Fetcher
from scripts.read_from_api.utils import url_to_id


def locations_etl(engine):
    locations_fetcher = Fetcher(LOCATIONS_TYPE)
    full_locations_df = locations_fetcher.query_to_pandas()
    locations_df = full_locations_df[['id', 'name', 'type', 'dimension']]
    locations_df = locations_df.rename(columns={'id': 'location_id'})
    locations_df.to_sql('locations', schema='storefirst', con=engine, if_exists='append', index=False)
    return full_locations_df


def _delete_no_status_residents(residents_df, characters):
    return residents_df[residents_df['character_id'].isin(characters['id'].apply(str))]


def create_residents_in_locations(engine, full_locations, characters):
    residents_df = full_locations[['id', 'residents']]
    residents_df = _clean_resident_ids(residents_df)
    residents_df = _delete_no_status_residents(residents_df, characters)
    residents_df = residents_df.reset_index(drop=True)
    residents_df.to_sql('residents_in_locations', schema='storefirst', con=engine, if_exists='append', index=False)


def _clean_resident_ids(residents_df):
    residents_df = residents_df.explode('residents')
    residents_df = residents_df[~residents_df['residents'].isnull()]
    residents_df['residents'] = residents_df['residents'].apply(url_to_id)
    residents_df = residents_df.rename(columns={'residents': 'character_id', 'id': 'location_id'})
    return residents_df
