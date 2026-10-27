#Multi-Product Shopping Budget Constraint
budget = float(input("Enter your shopping budget: "))
n = int(input("Enter number of products: "))

total = 0

if budget < 0 or n <= 0:
    print("Invalid input")
else:
    for i in range(n):
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid product details")
            break

        total += price * quantity
    else:
        print("Total Shopping Cost:", round(total, 2))

        if total <= budget:
            print("Shopping is within budget")
            print("Remaining Money:", round(budget - total, 2))
        else:
            print("Budget exceeded by:", round(total - budget, 2))