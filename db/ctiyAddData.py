import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="roott",
    port ="3308",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()
def _AddData(name, plateNo, URL):
    mycursor = mydb.cursor()
    sql = "INSERT INTO city (name, plateNo, URL) VALUES (%s, %s, %s)"
    val = (name, plateNo, URL)
    mycursor.execute(sql, val)
    mydb.commit()


