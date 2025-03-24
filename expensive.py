import csv

# File to store expenses
expense_file = "expenses.csv"

def add_expense():
    date = input("📅 Enter date (YYYY-MM-DD): ")
    category = input("📂 Enter category (Food, Transport, Bills, etc.): ")
    amount = input("💵 Enter amount: ")

    with open(expense_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(expense_file, mode="r") as file:
            reader = csv.reader(file)
            print("\n📊 Your Expenses:\n")
            for row in reader:
                print(f"📅 {row[0]} | 📂 {row[1]} | 💰 ₹{row[2]}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.\n")

while True:
    print("\n💰 Expense Tracker")
    print("1️⃣ Add Expense\n2️⃣ View Expenses\n3️⃣ Exit")
    choice = input("Select an option (1-3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Exiting... Stay financially smart! 💸")
        break
    else:
        print("⚠️ Invalid choice! Please enter 1-3.")
