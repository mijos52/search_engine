import mysql.connector as data_base

def db():

  mydb = data_base.connect(host = "localhost",user ="root",passwd ="1234",)

  print(mydb)

  