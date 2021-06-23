
import gspread
import mysql.connector



gc = gspread.service_account(filename='/home/rodrigues/Downloads/service_account.json')
sh = gc.open_by_key('1EJ8HkA95IGD6MMGapRv6Hf4x0vTlJH-feb0AR4kmxyo')

print(sh.sheet1.get('a2'))
print(sh.sheet1.get('b2'))
id = sh.sheet1.get('a2')
nome = sh.sheet1.get('b2')


print(id)
print(nome)

mydb = mysql.connector.connect(
  host="localhost",
  user="maca",
  password="maca123",
  database="oi"
)


mycursor = mydb.cursor()

sql = "INSERT INTO alunos (nome) VALUES (%s,%s);"
val = (id,nome)
print(sql)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")