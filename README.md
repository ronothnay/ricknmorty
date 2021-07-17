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
5. You can see the requested queries in the /queries folder

Have a nice day :)

### Scaling the architecture
Here are a few ideas for how to scale the system given there is a much larger data of episodes, characters and locations:
- **Partitions**:
The tables should be partitioned so the table scan would need (hopefully) only one partition scan. For instance, the episodes would be partitioned based on season_id, characters on origin.
- **Indexes**: Add HASH index on commonly "equal operator"-used columns across the tables: all the PKs of the tables, episode_code.
- **Views**: The seasons view would probably be too slow for regular usage. We could createa materialized view instead, or create a scheduled pipeline that will generate the most up-to-date seasons table every X time.
- **Updates**: The ETL would be needed to be able to support upserts on the tables, so that it wouldn't need to delete all the tables each time a new season arrives. It would also need to keep note of which data is new each time so as to not run on all the data each time.
- **Volume**: If the scale would be even larger, the current technologies used in these ETLs won't hold and we will need to introduce a parallelism paradigm using Spark or other technologies.
Many of the now simple queries would be needed to be more efficiently saved in specificly made tables made for these questions in the first place, using many more ETLs for each specific question.


