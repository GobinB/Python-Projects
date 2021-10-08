base = int(input("enter the base: "))
print(base)
exponent = int(input("enter the exponent: "))
print(exponent)

power = 1
i = 1

while (i <= exponent):
    power = power * base
    i = i + 1

print("The power is: = {2}".format(base, exponent, power))

