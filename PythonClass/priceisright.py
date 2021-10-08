if __name__ == "__main__":

    giResponse = 0
    while (giResponse != 6):
        print("\tTHE TRIVIA GAME")
        print("1\tPumpkin Spice Latte")
        print("2\tSoccer Ball")
        print("3\tWater Bottle")
        print("4\tAir Filter")
        print("5\tMask")
        print("6\tQuit")
        print("Enter your selection: ");
        giResponse = int(input())

        if (giResponse == 1):
            print("What is the price of a pumpkin spice latte?")
            answer = float(input())
            if (answer > 5.75):
                print("The price is wrong!")
            else:
                print("The price is right!")

        if (giResponse == 2):
            print("What is the price of a Soccer Ball?")
            answer = float(input())
            if (answer > 10.99):
                print("The price is wrong!")
            else:
                print("The price is right!")


        if (giResponse == 3):
            print("What is the price of a Water Bottle?")
            answer = float(input())
            if (answer > 7.49):
                print("The price is wrong!")
            else:
                print("The price is right!")


        if (giResponse == 4):
            print("What is the price of a Air Filter?")
            answer = float(input())
            if (answer > 14.28):
                print("The price is wrong!")
            else:
                print("The price is right!")


        if (giResponse == 5):
            print("What is the price of a Mask?")
            answer = float(input())
            if (answer > 2.99):
                print("The price is wrong!")
            else:
                print("The price is right!")



