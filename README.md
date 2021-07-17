# ricknmorty
By Ron Othnay for HiredScore.

### How to run?
1. Create venv according to setup.py
2. Install the latest PostgreSQL and add the database "ricknmorty". 
Notice to add your configurations on the file /config/connection_details//\_\_init\_\_.py
Change the following params to your likings:
 DB_NAME, 
 USER,
 PASSWORD,
 HOST.
3. Run the script /scripts/create_postgres_objects.py
4. Run the script /scripts/read_from_api/read_from_api.py
5. You can see the requested queries in the /queries.sql

Have a nice day :)