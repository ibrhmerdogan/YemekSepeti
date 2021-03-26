import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="roott",
    port ="3308",
    password="1234",
    database="ys"
)
mycursor = mydb.cursor()

def _SelectData():
    mycursor = mydb.cursor()
    mycursor.execute("select id,plateNo,URL,name from ys.fourcitydb where  plateNo = 34 and id<3952 and id>3781 ")
    myresult = mycursor.fetchall()
    return myresult
#x= _SelectData()
#for i in range(len(x)):
#    print(x[i][0]+"/restoran-arama",x[i][1])