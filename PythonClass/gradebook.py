userinput = int(input("Please enter the number of grades you wish to enter: "))

total_sum = 0

for i in range(userinput):
    grade = (float(input("please enter the grade: ")))
    total_sum += grade

    if grade >= 90:
        print("You got an A")
    if grade < 90 and grade >= 80:
        print("You got an B")

    if grade < 80 and grade >= 70:
        print("You got an C")

    if grade < 70 and grade >= 60:
        print("You got an D")

    elif grade < 60:
        print("You got an F")


average = (total_sum/userinput)

print("the average grade is: %0.2f" %average)

