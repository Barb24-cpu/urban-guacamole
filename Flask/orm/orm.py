#-connect to our db
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from dotenv import load_dotenv

#argument for the path to the .env file
load_dotenv()

class Database:

    def __init__(self):
        self.config={
            'dbname':os.getenv('DB_NAME'),
            'user':os.getenv('DB_USER'),
            'password':os.getenv('DB_PASSWORD'),
            'host':os.getenv('DB_HOST'),
            'port':os.getenv('DB_PORT')
        }

    @contextmanager
    def get_cursor(self):
        conn = psycopg2.connect(**self.config)
        # conn = psycopg2.connect(dbname=os.getenv('DB_NAME'),
        #                        user=os.getenv('DB_USER'))
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor #return the cursor to the context manager
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

#test the database connection individually
if __name__ == "__main__":
    print("Testing database connection...")
    try:
        db=Database()
        with db.get_cursor() as cursor:
            cursor.execute("SELECT NOW() as current_time, version();")
            result=cursor.fetchone()
            print(f"Database connection successful. Current time: {result['current_time']}, Version: {result['version']}")
    except Exception as e:
        print(f"Database connection failed: {e}")