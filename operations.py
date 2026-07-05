from datetime import datetime
import connection
import main
import statements
import queries
class App:
    def add_expense(self):
        
        user_date = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(user_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            self.add_expense()
        category = input("Enter the category: ")
        amount = input("Enter the amount: ")
        data_row = (date, category,amount)
        connection.create_table()
        connection.mycursor.execute(queries.add_data, data_row)
        connection.mydb.commit()
        main.obj.main_menu()
    def view_expense(self):
        
        connection.mycursor.execute(queries.get_data)
        expenses = connection.mycursor.fetchall()
        for expense in expenses:
            print(f'Expense No: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, Amount: {expense[3]}')
        main.obj.main_menu()
    def delete_expense(self):
        
        Delete_No = int(input('Enter Expense No to delete: '))
        if Delete_No > 0:
            connection.mycursor.execute(queries.delete, (Delete_No,))
            connection.mydb.commit()
            if connection.mycursor.rowcount:
                print(f'Expense No: {Delete_No} deleted successfully.')
            else:
                print('No matching expense was found.')
            
        main.obj.main_menu()
    def update_expense(self):
        
        Update_No = int(input('Enter a expense no that you want to Update :  '))
        u_date = input("Enter the date (YYYY-MM-DD): ")
        try:
            updated_date = datetime.strptime(u_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            self.update_expense()
        u_category = input("Enter the category: ")
        u_amount = float(input("Enter the amount: "))
        data = (updated_date,u_category,u_amount,Update_No)
        connection.mycursor.execute(queries.update,data)
        connection.mydb.commit()
        if connection.mycursor.rowcount:
            print('Expense Updated Successfully')
        else:
            print('Expense not found')
        main.obj.main_menu()
        
obj = App()