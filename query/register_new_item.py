from config import _get_db_connection

# MODELS
from psycopg2.errors import UniqueViolation


class ItemAlreadyExistDB(Exception):
    pass


def register_new_item_query(cod, name, brand, quantity):
    try:
        db = _get_db_connection()
        cursor = db.cursor()
        sql = "INSERT INTO items VALUES(%s, %s, %s, %s);"
        cursor.execute(sql, (cod, name, brand, quantity))
        db.commit()
        cursor.close()
        db.close()
    except UniqueViolation:
        raise ItemAlreadyExistDB
