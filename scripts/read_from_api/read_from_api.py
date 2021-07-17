from sqlalchemy import create_engine

from config.connection_details import URI
from scripts.read_from_api.create_characters import characters_etl


def main():
    engine = create_engine(URI)
    full_characters_df = characters_etl(engine)
    episodes_etl(engine)


if __name__ == '__main__':
    main()
