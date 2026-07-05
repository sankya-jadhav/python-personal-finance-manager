# Python Personal Finance Manager

## Overview

Python Personal Finance Manager is a command-line application developed using Python and MySQL. It helps users manage their daily expenses by allowing them to add, view, update, and delete expense records. The application also provides useful financial reports such as monthly spending, category-wise totals, highest expense, average expense, and total expenditure.

## Features

* Add a new expense
* View all expenses
* Update an existing expense
* Delete an expense
* Monthly spending report
* Category-wise expense report
* Highest expense
* Average expense
* Total expense calculation

## Technologies Used

* Python 3
* MySQL
* mysql-connector-python

## Project Structure

```text
connection.py      # Database connection
main.py            # Menu system
operations.py      # CRUD operations
queries.py         # SQL queries
statements.py      # Report generation
```

## Database Schema

Table: `expense`

| Column     | Type                              |
| ---------- | --------------------------------- |
| expense_id | INT (Primary Key, Auto Increment) |
| datetime   | DATE                              |
| category   | VARCHAR(255)                      |
| amount     | DECIMAL(10,2)                     |

## Installation

1. Clone the repository.
2. Install the required package:

```bash
pip install mysql-connector-python
```

3. Create a MySQL database named `F_Manager`.
4. Update the database credentials in `connection.py`.
5. Run `main.py`.

## Learning Outcomes

This project helped me practice:

* Python programming
* Object-Oriented Programming
* MySQL integration
* CRUD operations
* SQL aggregate functions
* Modular project structure
* Exception handling
* Database connectivity

## Future Improvements

* Search expenses
* Sort expenses
* Better input validation
* Export reports to CSV or Excel
* Graphical User Interface (GUI)
* Data visualization using Matplotlib
* Replace recursive menus with loop-based navigation
