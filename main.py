from datetime import datetime
import connection
class App:
    def __init__(self):
        pass
    def main_menu(self):
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("0. Exit")
        operation = input("Select an option: ")
        if operation == '1':
            self.add_expense()
        elif operation == '2':
            self.view_expense()
        elif operation == '3':
            self.delete_expense()
        elif operation == '4':
            self.update_expense()
        elif operation == 0:
            print("Exiting the application.")
            exit()
        else:
            print('Invalid choice. Please try again.')
    def add_expense(self):
        user_date = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(user_date, '%Y-%m-%d')
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
            self.add_expense()
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        data_row = (date, category,amount)
        connection.create_table()
        connection.mycursor.execute(connection.query, data_row)
        connection.mydb.commit()
        self.main_menu()
    def view_expense(self):
        connection.mycursor.execute(connection.get_data)
        expenses = connection.mycursor.fetchall()
        for expense in expenses:
            print(f'Expense No: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, Amount: {expense[3]}')
        self.main_menu()
    def delete_expense(self):
        Delete_No = int(input('Enter Expense No to delete: '))
        if Delete_No > 0:
            connection.mycursor.execute(connection.delete, (Delete_No,))
            connection.mydb.commit()
            print(f'Expense No: {Delete_No} deleted successfully.')
        self.main_menu()
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
        connection.mycursor.execute(connection.update,data)
        connection.mydb.commit()
        
        
obj = App()
obj.main_menu()