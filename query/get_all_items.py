from config import _get_db_connection


def _get_all_items():
    db = _get_db_connection()
    cursor = db.cursor()
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    all_items = cursor.fetchall()
    return all_items
