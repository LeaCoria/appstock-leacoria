from config import _get_db_connection


def _substract_quantity(quantity_to_substract, current_quantity, cod):
    try:
        quantity = int(current_quantity) - int(quantity_to_substract)
        db = _get_db_connection()
        cursor = db.cursor()
        sql = "UPDATE items SET quantity = %s WHERE cod = %s;"
        cursor.execute(sql, (quantity, cod))
        db.commit()
        cursor.close()
        db.close()
    except Exception as ex:
        raise ex
