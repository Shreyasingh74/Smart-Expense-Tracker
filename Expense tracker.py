import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "myexpenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

def add_transaction():
    date = datetime.now().strftime("%Y-%m-%d")

    t_type = input("Enter type (Income/Expense): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, description])

    print("Transaction added successfully!")

def view_transactions():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n===== All Transactions =====")
        for row in reader:
            print(row)

def show_balance():
    income = 0
    expense = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Type"].lower() == "income":
                income += float(row["Amount"])
            elif row["Type"].lower() == "expense":
                expense += float(row["Amount"])

    print("\n===== Balance Summary =====")
    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Balance      :", income - expense)

def show_chart():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Type"].lower() == "expense":
                category = row["Category"]
                amount = float(row["Amount"])

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

    if len(categories) == 0:
        print("No expense data found!")
        return

    plt.bar(categories.keys(), categories.values())
    plt.title("Expense Analysis")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def monthly_report():
    month = input("Enter month number (01-12): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== Monthly Expense Report =====")

        for row in reader:
            date = row["Date"]
            transaction_month = date[5:7]

            if transaction_month == month and row["Type"].lower() == "expense":
                print(row)
                total += float(row["Amount"])

    print("Total Expense in this month:", total)

def main():
    create_file()

    while True:
        print("\n===== Smart Expense Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Show Expense Chart")
        print("5. Monthly Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            monthly_report()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()