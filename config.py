from psycopg2 import connect
from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config:
    SECRET_KEY = "B!iwcNAt1^%kvhUI*S^"


class DevelopmentConfig(Config):
    DEBUG = True


MYSQL_HOST = environ.get('DB_HOST')
MYSQL_PORT = environ.get('DB_PORT')
MYSQL_USER = environ.get('DB_USER')
MYSQL_PASSWORD = environ.get('DB_PASSWORD')
MYSQL_DB = environ.get('DB_NAME')


def _get_db_connection():
    db = connect(host=MYSQL_HOST, port=MYSQL_PORT, dbname=MYSQL_DB,
                 user=MYSQL_USER, password=MYSQL_PASSWORD)
    return db


config = {
    'development': DevelopmentConfig
}
