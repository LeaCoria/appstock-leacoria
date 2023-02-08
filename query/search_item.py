from config import _get_db_connection
from models.entities.Item import Item


def search_item(cod):
    try:
        db = _get_db_connection()
        cursor = db.cursor()
        sql = "SELECT * FROM items WHERE cod = %s;"
        cursor.execute(sql, (cod, ))
        row = cursor.fetchone()
        item = Item(row[0], row[1], row[2], row[3])
        return item
    except Exception as ex:
        raise ex
