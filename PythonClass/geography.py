d = {}
score = 0

for i in range(10):
    countries = str(input("Please enter a country: "))
    capital = str(input("lease enter the capital: "))

    d[countries] = capital


for k, v in d.items():
    askingcap = str(input("What is the capital of %s" % k))
    if askingcap == v:
        print("you got it")
        score += 1
        print("current score is: ", score)

    else:
        print("you got it wrong")
        score -= 1
        print("current score is: ", score)


print("Final score is: ", score)


