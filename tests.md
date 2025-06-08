# Manual Test Plan for Simple Budget Tracker

## Test 1: Add income
- Action: Choose option 1, enter 1000 and "Salary".
- Expected: "Transaction added." message.
- Then list: should show 1000 and "Salary".

## Test 2: Add expense
- Action: Add -200 with description "Groceries".
- Expected: Balance should be 800.

## Test 3: View transactions
- Action: Choose option 2.
- Expected: Should list all added items with correct amounts and descriptions.

## Test 4: View balance
- Action: Choose option 3.
- Expected: Shows current balance as sum of all transactions.

## Test 5: Invalid input
- Action: Enter "abc" for amount.
- Expected: Shows error "Invalid amount. Try again."

## Test 6: Exit
- Action: Choose option 4.
- Expected: Program ends with "Goodbye!"
