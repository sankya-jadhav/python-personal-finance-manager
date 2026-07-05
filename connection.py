import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Root@123",
database='F_Manager'
)
mycursor = mydb.cursor()
def create_table():
    mycursor.execute("CREATE TABLE If not exists expense (expense_id INT AUTO_INCREMENT PRIMARY KEY, datetime DATE, category Varchar (255),amount Decimal(10,2))")


