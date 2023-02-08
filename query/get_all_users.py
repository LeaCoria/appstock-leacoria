from config import _get_db_connection


def _get_all_users():
    db = _get_db_connection()
    cursor = db.cursor()
    sql = "SELECT email, username, name, lastname, admin FROM users"
    cursor.execute(sql)
    all_users = cursor.fetchall()
    return all_users
