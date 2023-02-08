from config import _get_db_connection

# MODELS
from psycopg2.errors import UniqueViolation


class EmailAlreadyExistDB(Exception):
    pass


class UserAlreadyExistDB(Exception):
    pass


def create_user(email, password, username, name, last_name) -> None:
    try:
        db = _get_db_connection()
        cursor = db.cursor()
        sql_insert = """INSERT INTO users VALUES(DEFAULT,
        %s, %s, %s, %s, %s, FALSE);"""
        data = (email, password, username, name, last_name)
        cursor.execute(sql_insert, data)
        db.commit()
        cursor.close()
        db.close()
    except UniqueViolation as unique_violation:
        if 'username' in unique_violation.args[0]:
            raise UserAlreadyExistDB
        else:
            raise EmailAlreadyExistDB
