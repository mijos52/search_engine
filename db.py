import mysql.connector as data_base

'''
db creates a database connection


'''

database_name = "database_one"
table_name = "table_one"
create_db = f'CREATE DATABASE {database_name}'
show_db = 'SHOW DATABASES'

table_customers = f'CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, meta_data VARCHAR(255),' \
                  f' key_words VARCHAR(255), links VARCHAR(255))'
alter_tables = f'ALTER TABLE {table_name} ADD COLUMN meta_data VARCHAR(255)'


def db_write_multiple(val):
    my_db = data_base.connect(host="localhost", user="root", passwd="1234", database=database_name)
    my_cursor = my_db.cursor()

    insert_table = f'INSERT INTO {table_name} (meta_data, key_words,links) VALUES (%s,%s,%s)'

    # sql query will go inside .execute
    my_cursor.execute(insert_table, val)

    # writing into rows
    my_db.commit()
    print(my_cursor.rowcount, "record inserted.")


def db_read():
    my_db = data_base.connect(host="localhost", user="root", passwd="1234", database=database_name)
    my_cursor = my_db.cursor()

    fetch_data = f'SELECT meta_data, key_words, links FROM {table_name}'

    # sql query will go inside .execute
    my_cursor.execute(fetch_data)

    # read from the database
    result = my_cursor.fetchall()

    for i in result:
        print(i)


def db_show_table():
    my_db = data_base.connect(host="localhost", user="root", passwd="1234", database=database_name)
    my_cursor = my_db.cursor()

    show_tables = 'SHOW TABLES'

    # sql query will go inside .execute
    result = my_cursor.execute(show_tables)

    print(result)



