#Examination Result and Grace-Mark Validation 
marks = int(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    if marks >= 35:
        print("Result: Pass")
    elif marks >= 30:
        marks = marks + 5
        print("Grace marks added: 5")
        print("Final Marks:", marks)
        print("Result: Pass")
    else:
        print("Result: Fail")