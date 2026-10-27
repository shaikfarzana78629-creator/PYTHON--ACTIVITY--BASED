#Campus Event Financial Planning
budget = float(input("Enter the total budget: "))
venue = float(input("Enter venue cost: "))
food = float(input("Enter food cost: "))
decoration = float(input("Enter decoration cost: "))
other = float(input("Enter other expenses: "))

total = venue + food + decoration + other
balance = budget - total

print("Total Expenses:", total)

if balance >= 0:
    print("Remaining Budget:", balance)
    print("Event is within budget")
else:
    print("Budget exceeded by:", abs(balance))