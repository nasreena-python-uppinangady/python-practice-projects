# Personal Expense Tracker - by Fathimath Nasreena K
# A simple tool to track daily expenses - WFH Job Ready Project

expenses = []

def add_expense(amount, category, note=""):
    expense = {"amount": amount, "category": category, "note": note}
    expenses.append(expense)
    print(f"Added: Rs.{amount} for {category}")

def view_expenses():
    if not expenses:
        print("No expenses yet!")
        return
    total = 0
    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Rs.{exp['amount']} - {exp['category']} ({exp['note']})")
        total += exp['amount']
    print(f"\nTotal Spent: Rs.{total}")

def total_by_category():
    totals = {}
    for exp in expenses:
        totals[exp['category']] = totals.get(exp['category'], 0) + exp['amount']
    print("\n--- Total by Category ---")
    for cat, amt in totals.items():
        print(f"{cat}: Rs.{amt}")

# Main Program
while True:
    print("\n1. Add Expense | 2. View Expenses | 3. View by Category | 4. Exit")
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        amt = float(input("Enter amount: Rs."))
        cat = input("Enter category (Food/Travel/Shopping): ")
        note = input("Enter note: ")
        add_expense(amt, cat, note)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_by_category()
    elif choice == "4":
        print("Thank you! Keep tracking!")
        break
    else:
        print("Invalid choice!")
