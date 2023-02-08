from config import _get_db_connection


def _add_quantity(quantity_to_add, current_quantity, cod):
    try:
        quantity = int(quantity_to_add) + int(current_quantity)
        db = _get_db_connection()
        cursor = db.cursor()
        sql = "UPDATE items SET quantity = %s WHERE cod = %s;"
        cursor.execute(sql, (quantity, cod))
        db.commit()
        cursor.close()
        db.close()
    except Exception as ex:
        raise ex
