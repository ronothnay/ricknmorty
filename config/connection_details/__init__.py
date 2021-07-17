DB_NAME = "ricknmorty"
USER = "postgres"
PASSWORD = "admin"
HOST = "127.0.0.1"

URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:5432/{DB_NAME}"

TABLES_FOLDER = 'tables'
VIEWS_FOLDER = 'views'
SCHEMAS_FOLDER = 'schemas'
DROPS_FOLDER = 'drop'

SQL_OBJECTS_PATH = r"..\sql_objects\{object_type}\{file_name}"

PRIMARY_TABLES = ['characters.sql', 'episodes.sql', 'locations.sql']
SECONDARY_TABLES = ['characters_in_episodes.sql', 'residents_in_locations.sql']
VIEWS = ['seasons.sql']
SCHEMAS = ['storefirst_schema.sql']
DROPS = ['drop_tables.sql']
