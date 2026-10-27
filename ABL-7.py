
# Traffic Violation Penalty Calculator

print("1. No Helmet")
print("2. Overspeeding")
print("3. No Seat Belt")
print("4. Signal Violation")

choice = int(input("Enter violation type: "))

if choice == 1:
    fine = 500
elif choice == 2:
    fine = 1000
elif choice == 3:
    fine = 500
elif choice == 4:
    fine = 1000
else:
    fine = -1

if fine == -1:
    print("Invalid violation type")
else:
    print("Traffic Penalty: Rs.", fine)
