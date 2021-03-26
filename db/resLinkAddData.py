import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="roott",
    port ="3308",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()
def _AddData(plateNo,newORold,openORClosed,deliveryTime,headRate,resURL,headText,resStatus,resName,district):
    mycursor = mydb.cursor()
    sql = "INSERT INTO reslinkant (plateNo,deliveryTime,headRate,resURL,headText,resStatus,resName,newORold,openORClosed,district) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (plateNo,deliveryTime,headRate,resURL,headText,resStatus,resName,newORold,openORClosed,district)
    mycursor.execute(sql, val)
    mydb.commit()


