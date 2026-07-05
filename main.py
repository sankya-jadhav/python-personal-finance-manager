import operations
import statements
class menus:
    def main_menu(self):
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Update Expense")
            print("5. Fetch Expenses")
            print("0. Exit")
            operation = int(input("Select an option: "))
            if operation == 1:
                operations.obj.add_expense()
            elif operation == 2:
                operations.obj.view_expense()
            elif operation == 3:
                operations.obj.delete_expense()
            elif operation == 4:
                operations.obj.update_expense()
            elif operation == 5:
                self.fetching()
            elif operation == 0:
                print("Exiting the application.")
                exit()
            else:
                print('Invalid choice. Please try again.')
    def fetching(self):
        print("1. Monthly Spending Report")
        print("2. Highest Expense")
        print('3. Category-wise Expense Report')
        print('4. Average expense report')
        print('5.Total expense ')
        print('6. Main Menu')
        print('Other to Exits')
        operation = input("Select an option: ")
        if operation == '1':
            statements.obj.monthly_spending()
        elif operation == '2':
            statements.obj.highest_expense()
        elif operation == '3':
            statements.obj.category_wise_expense()
        elif operation == '4':
            statements.obj.average_expense()
        elif operation == '5':
            statements.obj.total_expense()
        elif operation == '6':
            self.main_menu()
        else:
            exit()
        
obj = menus()
if __name__ == "__main__":
    obj.main_menu()