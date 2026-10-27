#Attendance Recovery Computation
held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
target = 75

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance details")
else:
    percentage = attended / held * 100
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage >= target:
        print("Attendance requirement satisfied")
    else:
        required = 0
        while (attended + required) / (held + required) * 100 < target:
            required += 1

        print("Additional classes to attend:", required)