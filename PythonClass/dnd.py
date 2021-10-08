import random

strength = int(input("Enter monster strength: "))
print(strength)


def tossdie():
    rolldie = random.randrange(20) + 1
    print("you rolled: ", rolldie)

    if rolldie > 17 and rolldie > strength:
        print("critical hit")

    if rolldie < 3 and rolldie < strength:
        print("critical fail")

    if rolldie == strength:
        print("Tie")

    else:
        if rolldie < 18 and rolldie > strength:
            print("Hit")
        if rolldie >= 3 and rolldie < strength:
            print("Fail")






tossdie()

