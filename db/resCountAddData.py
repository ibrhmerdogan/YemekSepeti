import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="roott",
    port ="3308",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()
def _AddData(count,plateNo,reg_date,name):
    mycursor = mydb.cursor()
    sql = "INSERT INTO reCount (count,plateNo,reg_date,name) VALUES (%s, %s, %s, %s)"
    val = (count,plateNo,reg_date,name)
    mycursor.execute(sql, val)
    mydb.commit()


