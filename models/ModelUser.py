from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0],
                            row[3],
                            User.check_password(row[2], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise ex

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row is not None:
                sql2 = """SELECT CONCAT(name, ' ', lastname) AS
                fullname FROM users WHERE id = %s"""
                cursor.execute(sql2, (id,))
                row2 = cursor.fetchone()
                return User(row[0],
                            row[3],
                            None,
                            row[6],
                            row[1],
                            row[4],
                            row[5],
                            row2[0])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
