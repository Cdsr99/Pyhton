import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="maca",
  password="maca123",
  database="oi"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nome FROM alunos")

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 






