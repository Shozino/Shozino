import datetime

transactions = []

def add_transaction(amount, description):
    transaction = {
        "amount": amount,
        "description": description,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)

def get_balance():
    return sum(t["amount"] for t in transactions)

def list_transactions():
    return transactions

def print_summary():
    print("\n---- Summary ----")
    for t in transactions:
        print(f"{t['date']}: {t['description']} - {t['amount']}")
    print(f"Current balance: {get_balance():.2f}\n")

def main():
    print("Welcome to Budget Tracker")
    while True:
        print("Options: 1) Add  2) List  3) Balance  4) Quit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            try:
                amount = float(input("Enter amount (+income, -expense): "))
                desc = input("Enter description: ")
                add_transaction(amount, desc)
                print("Transaction added.\n")
            except ValueError:
                print("Invalid amount. Try again.\n")
        elif choice == '2':
            print_summary()
        elif choice == '3':
            print(f"Balance: {get_balance():.2f}\n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
