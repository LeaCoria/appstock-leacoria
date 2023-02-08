def _create_table_items(db):
    cursor = db.cursor()
    sql_items = """CREATE TABLE items (cod varchar(30) NOT NULL UNIQUE,
    name varchar (50) NOT NULL, brand varchar(30) NOT NULL,
    quantity int NOT NULL);"""
    cursor.execute(sql_items)
    db.commit()
    cursor.close()


def _create_table_users(db):
    cursor = db.cursor()
    sql_users = """CREATE TABLE users (ID SERIAL PRIMARY KEY
    NOT NULL , email varchar(50) NOT NULL UNIQUE, password char(102)
    NOT NULL, username varchar(20) NOT NULL UNIQUE, name varchar(30) NOT NULL,
    lastname varchar(30) NOT NULL, admin boolean NOT NULL);"""
    cursor.execute(sql_users)
    db.commit()
    cursor.close()


def _insert_admin(db):
    cursor = db.cursor()
    sql_insert_user = """INSERT INTO users (ID, email, password,
    username, name, lastname, admin) VALUES (DEFAULT, 'admin@admin.com',
    'pbkdf2:sha256:260000$nHnHXRUspx5xbjMY$5b99d07de141baa74f3704cb098a5c635c3c44291eaa572ad3978853e2e6f4e3',
    'admin', 'admin', 'admin', TRUE);"""
    cursor.execute(sql_insert_user)
    db.commit()
    cursor.close()


def _insert_items(db):
    cursor = db.cursor()
    sql_insert_items = """INSERT INTO items (cod, name,brand,
    quantity) VALUES ('SIN-130003-01', 'Xileno', 'Sintorgan', 20),
    ('918110', 'Ácido Clorhídrico', 'Cicarelli', 5),
    ('9803.08', 'Hidrógeno Peróxido', 'Biopack', 3),
    ('FT-3-101-125', 'Papel de filtro', 'Sartorius', 5);"""
    cursor.execute(sql_insert_items)
    db.commit()
    cursor.close()
