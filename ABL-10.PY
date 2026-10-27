#Courier Charge Optimization
weight = float(input("Enter parcel weight in kg: "))

if weight <= 0:
    print("Invalid parcel weight")
else:
    # Courier 1: Rs. 50 base + Rs. 20 per kg
    charge1 = 50 + weight * 20

    # Courier 2: Rs. 70 base + Rs. 15 per kg
    charge2 = 70 + weight * 15

    print("Courier 1 Charge: Rs.", round(charge1, 2))
    print("Courier 2 Charge: Rs.", round(charge2, 2))

    if charge1 < charge2:
        print("Courier 1 is cheaper")
        print("You save Rs.", round(charge2 - charge1, 2))
    elif charge2 < charge1:
        print("Courier 2 is cheaper")
        print("You save Rs.", round(charge1 - charge2, 2))
    else:
        print("Both couriers have equal charges")