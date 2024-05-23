import os
import sqlite3
import pandas as pd # type: ignore
from utils import logger
from .loader import Loader

class SQLiteLoader(Loader):

    def load_data(self, read_from, write_to, database_name):
        
        database_path = os.path.join(write_to, database_name) 
        
        if not os.path.exists(database_path):
            os.mkdir(write_to)
            logger.info(f"Database {database_name} did not exist and was created.")
        else:
            logger.info(f"Database {database_name} exists. Connected successfully.")

        conn = sqlite3.connect(database_path)

        try:
            for filename in os.listdir(read_from):
                if filename.endswith(".csv"):
                    table_name = os.path.splitext(filename)[0]
                    file_path = os.path.join(read_from, filename)

                    data = pd.read_csv(file_path)

                    data.to_sql(table_name, conn, if_exists='replace', index=False)
                    logger.info(f"Data from {file_path} loaded into {table_name} table in {database_name} database.")

            conn.commit()

        except Exception as ex:
            logger.error(f"An exception occurred: {ex}")

        finally:
            if conn:
                conn.close()
                logger.info(f"Connection to {database_name} closed.")
