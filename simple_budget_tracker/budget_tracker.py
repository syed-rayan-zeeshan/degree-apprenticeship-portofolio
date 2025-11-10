# Simple Budget Tracker (Beginner Version)
# Tracks income, expenses, balance, and category totals using JSON

import json
import os

# Get folder path
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, "budget_data.json")

# Load existing data or create empty structure
if os.path.exists(data_file):
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = {"income": [], "expenses": []}

# Function to save data
def save_data():
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Function to add income
def add_income():
    amount = float(input("Enter income amount: "))
    desc = input("Enter description: ")
    data["income"].append({"amount": amount, "description": desc})
    save_data()
    print("Income added successfully!\n")

# Function to add expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    desc = input("Enter description: ")
    data["expenses"].append({"amount": amount, "category": category, "description": desc})
    save_data()
    print("Expense added successfully!\n")

# Function to show balance
def show_balance():
    total_income = sum(i["amount"] for i in data["income"])
    total_expense = sum(e["amount"] for e in data["expenses"])
    balance = total_income - total_expense
    print(f"\nCurrent balance: {balance}\n")

# Function to show expenses by category
def show_expenses_by_category():
    categories = {}
    for e in data["expenses"]:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]
    print("\nExpenses by Category:")
    for cat, amount in categories.items():
        print(f"{cat}: {amount}")
    print()

# Main menu
def main():
    while True:
        print("Welcome to Simple Budget Tracker!")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Expenses by Category")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            show_expenses_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.\n")

if __name__ == "__main__":
    main()
