import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="roott",
    port ="3308",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()
def _AddData(plateNo,URL,count,name):
    mycursor = mydb.cursor()
    sql = "INSERT INTO fourCityDB (plateNo,URL,count,name) VALUES (%s, %s, %s, %s)"
    val = (plateNo,URL,count,name)
    mycursor.execute(sql, val)
    mydb.commit()


