#Student Timetable Conflict Detection 
day1 = input("Enter day of first class: ").lower()
start1 = int(input("Enter first class start time (minutes): "))
end1 = int(input("Enter first class end time (minutes): "))

day2 = input("Enter day of second class: ").lower()
start2 = int(input("Enter second class start time (minutes): "))
end2 = int(input("Enter second class end time (minutes): "))

if (start1 < 0 or end1 > 1440 or start2 < 0 or end2 > 1440
        or start1 >= end1 or start2 >= end2):
    print("Invalid time")
elif day1 == day2 and start1 < end2 and start2 < end1:
    print("Timetable Conflict Detected")
else:
    print("No Timetable Conflict")
