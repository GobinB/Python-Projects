import sys

print("Welcome to the ATM!")

global startingBal
currentBal = 0
startingBal = float(input("Please enter starting balance: "))
currentBal = startingBal
print("current balance: ", currentBal)

# making deposit function 
def deposit():
    global currentBal
    depo = float(input("Please enter deposit: "))
    currentBal += depo
    print("updated balance: ", currentBal)

# making Withdrawl function

def withdraw():
    global currentBal
    withDr = float(input("Enter your withdraw ammount: "))
    if withDr > currentBal:
        print("overdrawn")
        sys.exit()
    else:
       currentBal -= withDr
       print("updated balance: ", currentBal)
    #  currentBal -= withDr



while currentBal >= 0:
     option = int(input("choose option [1] for Deposit. [2] for Withdraw: "))
     if option == 1:
        deposit()
     if option == 2:
        withdraw()


