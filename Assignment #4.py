#Create Expense List
Expense_Report = []
Expense = 1
while Expense != 0:
    Expense = float(input("Enter and expense. If you have no more expenses, type a 0:  "))
    Expense = round(Expense,2)
    if Expense != 0:
        Expense_Report.append(Expense)

#Calculations
num_expenses = len(Expense_Report)
sum_expenses = sum(Expense_Report)
avg_expense = round(sum_expenses/num_expenses,2)
smallest_expense = min(Expense_Report)
largest_expense = max(Expense_Report)

#Count Expense Sizes
Small = 0
Moderate = 0
Large = 0
for response in Expense_Report:
    if response < 25:
        Small += 1
    elif response <=100:
        Moderate += 1
    else:
        Large += 1

#Print Summary
print("")
print("")
print("Expense Summary")
print("----------------")
print(f"Number of Expenses {num_expenses}")
print(f"Sum of Expenses {sum_expenses}")
print(f"Average Expense Size {avg_expense}")
print(f"Smallest Expense {smallest_expense}")
print(f"Largest Expense {largest_expense}")
print("----------------")
print(f"Small Expenses {Small}")
print(f"Moderate Expenses {Moderate}")
print(f"Large Expenses {Large}")


