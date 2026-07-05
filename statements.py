import connection
import main
import queries
class Operations:
    def monthly_spending(self):
        
        connection.mycursor.execute(queries.m_query);
        rows = connection.mycursor.fetchall()
        for row in rows:
            print(f'Month : {row[0]} , Monthly_spending : {row[1]}')
        main.obj.feaching()
    def highest_expense(self):
        
        connection.mycursor.execute(queries.h_query);
        rows = connection.mycursor.fetchall()
        for row in rows:
            print(f'Expense No: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: {row[3]}')
        main.obj.feaching()
    def category_wise_expense(self):
       
        connection.mycursor.execute(queries.c_query);
        rows = connection.mycursor.fetchall()
        for row in rows:
            print(f'Category: {row[0]}, Total Amount: {row[1]}')
        main.obj.feaching()
    def average_expense(self):
        
        connection.mycursor.execute(queries.a_query);
        rows = connection.mycursor.fetchall()
        for row in rows:
            print(f'Average Amount: {row[0]}')
        main.obj.feaching()
    def total_expense(self):
        
        connection.mycursor.execute(queries.t_query);
        rows = connection.mycursor.fetchall()
        for row in rows:
            print(f'Total Amount: {row[0]}')
        main.obj.feaching()
              
obj = Operations()
