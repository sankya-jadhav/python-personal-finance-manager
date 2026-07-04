import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Root@123",
database='F_Manager'
)

mycursor = mydb.cursor()
query = "INSERT INTO expense (datetime, category, amount) VALUES (%s, %s, %s)"
get_data ="SELECT * FROM expense"
delete ="DELETE FROM expense WHERE expense_id = %s"
update ="Update expense SET datetime= %s,category= %s,amount= %s where expense_id = %s"
def create_table():
    mycursor.execute("CREATE TABLE If not exists expense (expense_id INT AUTO_INCREMENT PRIMARY KEY, datetime DATE, category Varchar (255),amount Decimal(10,2))")


