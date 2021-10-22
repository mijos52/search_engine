import mysql.connector as data_base

'''
db creates a database connection


'''
input_db = 'CREATE DATABASE my_database'
show_db = 'SHOW DATABASES'


def db():
    my_db = data_base.connect(host="localhost", user="root", passwd="1234", database="my_database")
    print(my_db)

    my_cursor = my_db.cursor()

    # sql query will go inside .execute
    # data_out = my_cursor.execute(input_db, show_db)
    # print(data_out)
    #
    # for i in data_out:
    #     print(i)
