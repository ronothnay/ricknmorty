from sqlalchemy import create_engine

from config.connection_details import URI
from scripts.read_from_api.create_characters import characters_etl, create_characters_to_episodes
from scripts.read_from_api.create_episodes import episodes_etl
from scripts.read_from_api.create_locations import locations_etl, create_residents_in_locations

import scripts.create_postgres_objects as initialize

def main():
    engine = create_engine(URI)
    run_workflow(engine)


def run_workflow(engine):
    full_characters_df = characters_etl(engine)
    episodes_etl(engine)
    create_characters_to_episodes(engine, full_characters_df)
    locations_df = locations_etl(engine)
    create_residents_in_locations(engine, locations_df, full_characters_df)


if __name__ == '__main__':
    main()
