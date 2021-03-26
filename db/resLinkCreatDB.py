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
        "CREATE TABLE resLinkAnt (id INT AUTO_INCREMENT PRIMARY KEY,plateNo VARCHAR(255), deliveryTime VARCHAR(255), headRate VARCHAR(255), resURL VARCHAR(255), headText VARCHAR(255), resStatus VARCHAR(255), resName VARCHAR(255),newORold VARCHAR(255),openORClosed VARCHAR(255),district VARCHAR(255))")
    print("tablo oluşturuldu")

