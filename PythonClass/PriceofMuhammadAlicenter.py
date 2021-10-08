

print("Welcome to the Muhammad Ali Center")


# $14 for adults
# $13 for seniors 65+
# $10 for military or student with ID
# $9 for children age 6-12
# Free for children under 5
# Calculate the price of a family entering the museum


def adults(adult, millstudent):
    discount = int(input("Is this person a member of the military or a student with ID? Enter [1] if yes, [0] if no:  "))
    if discount == 1:
        print("The price is ${:.2f}".format(millstudent))
        return millstudent

    if discount == 0:
        print("The price is ${:.2f}".format(adult))
        return adult


def seniors(senior, millstudent):
    discount = int(input("Is this person a member of the military or a student with ID? Enter [1] if yes, [0] if no:  "))
    if discount == 1:
        print("The price is ${:.2f}".format(millstudent))
        return millstudent

    if discount == 0:
        print("The price is ${:.2f}".format(senior))
        return senior


def childrens(children):
    print("The price is ${:.2f}".format(children))
    return children


def underfives(underfive):
    print("The price is free")
    return underfive



def main():
    adult = 14
    senior = 13
    millstudent = 10
    children = 9
    underfive = 0
    total = 0

    while True:
        age = int(input("Enter the age of your family members: "))
        print(age)

        if age >= 13 and age < 65:
            total += adults(adult, millstudent)


        if age >= 65:
            total += seniors(senior, millstudent)

        if age >= 6 and age < 13:
            total += childrens(children)

        if age <= 5:
            total += underfives(underfive)

        addMembers = int(input("Are you finished? If yes, type [1], else, type [0]: "))
        if addMembers == 0:
            continue
        else:
            print('this is total after finished: ', total)
            totalsum = ("The total is ${:.2f}".format(total))
            print(totalsum)
        break


main()


