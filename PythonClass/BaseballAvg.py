
print("Please enter the hits for when Player X steps to the plate. Type 'done' when finished")

hit = 0
walk = 0
strikeout = 0
while True:
    userInput = str(input("Please enter 'hit', 'walk', 'strikeout', or done: "))
    print(userInput)
    if userInput == 'hit':
        hit += 1
    if userInput == 'walk':
        walk += 1
    if userInput == 'strikeout':
        strikeout += 1

    if userInput == 'done':
        avg = hit/(hit + walk + strikeout)
        print(avg)




