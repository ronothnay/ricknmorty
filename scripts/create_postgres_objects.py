import logging

import psycopg2
import config.connection_details as conn


def get_sql(object_type, file_name):
    with open(conn.SQL_OBJECTS_PATH.format(object_type=object_type, file_name=file_name),
              'r') as file:
        return file.read()


def execute_files(connection, object_type, file_names):
    with connection.cursor() as cursor:
        for file_name in file_names:
            try:
                sql = get_sql(object_type, file_name)
                cursor.execute(sql)
            except Exception as er:
                logging.warning(f"The SQL file {file_name} couldn't be run")
                raise er
    connection.commit()


def main():
    with psycopg2.connect(dbname=conn.DB_NAME,
                          user=conn.USER,
                          password=conn.PASSWORD,
                          host=conn.HOST) as connection:
        execute_files(connection, conn.SCHEMAS_FOLDER, conn.SCHEMAS)
        execute_files(connection, conn.TABLES_FOLDER, conn.PRIMARY_TABLES)
        execute_files(connection, conn.TABLES_FOLDER, conn.SECONDARY_TABLES)
        execute_files(connection, conn.VIEWS_FOLDER, conn.VIEWS)


if __name__ == '__main__':
    main()
