#Fuel Consumption and Route Comparison 
distance1 = float(input("Enter distance of Route 1 (km): "))
distance2 = float(input("Enter distance of Route 2 (km): "))
mileage = float(input("Enter vehicle mileage (km/l): "))
price = float(input("Enter fuel price per litre: "))

if distance1 <= 0 or distance2 <= 0 or mileage <= 0 or price < 0:
    print("Invalid input")
else:
    fuel1 = distance1 / mileage
    fuel2 = distance2 / mileage

    cost1 = fuel1 * price
    cost2 = fuel2 * price

    print("Route 1 Fuel:", round(fuel1, 2), "litres")
    print("Route 1 Cost:", round(cost1, 2))

    print("Route 2 Fuel:", round(fuel2, 2), "litres")
    print("Route 2 Cost:", round(cost2, 2))

    if cost1 < cost2:
        print("Route 1 is cheaper")
    elif cost2 < cost1:
        print("Route 2 is cheaper")
    else:
        print("Both routes have equal fuel cost")