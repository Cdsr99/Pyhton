import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="maca",
  password="maca123",
  database="oi"
)

id = 9
nome = "carlito"

mycursor = mydb.cursor()

sql = "INSERT INTO alunos (id, nome) VALUES (%s, %s)"
val = (id, nome)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")