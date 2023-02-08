from config import _get_db_connection


def unmake_admin_query(username):
    db = _get_db_connection()
    cursor = db.cursor()
    sql = "UPDATE users SET admin = FALSE WHERE username = %s"
    cursor.execute(sql, (username,))
    db.commit()
    cursor.close()
    db.close()
