import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port = "3308",
    user="root",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()


def _CreatorTable():
    mycursor.execute(
        "CREATE TABLE fourCityDB (id INT AUTO_INCREMENT PRIMARY KEY,plateNo VARCHAR(255), URL VARCHAR(255), count VARCHAR(255), name VARCHAR(255))")
    print("tablo oluşturuldu")

