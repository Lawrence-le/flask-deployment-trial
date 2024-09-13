from flask import current_app
import psycopg

def get_db_connection():
    # Ensure this is called within an application/request context
    db_url = current_app.config['DATABASE_URL']
    conn = psycopg.connect(db_url)
    return conn
