#Laboratory Chemical Inventory Validation
available = float(input("Enter available chemical quantity (ml): "))
required = float(input("Enter required quantity (ml): "))
minimum = float(input("Enter minimum stock level (ml): "))

if available < 0 or required < 0 or minimum < 0:
    print("Invalid quantity")
else:
    if available >= required:
        remaining = available - required
        print("Experiment can be conducted")
        print("Remaining Chemical:", remaining, "ml")

        if remaining < minimum:
            print("Warning: Chemical stock is low")
        else:
            print("Chemical stock is sufficient")
    else:
        shortage = required - available
        print("Insufficient chemical")
        print("Additional quantity needed:", shortage, "ml")