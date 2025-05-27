#james bowey
#1/28/25
#slot machine

#init
import random
import time
symbols = ["7", "♬", "♬", "♠", "♠", "▼", "▼", "⚡", "⚡"]   #slot list
print("Welcome to your slot machine; spin 3 7's for a jackpot or 2-3 matching symbols (♬, ♠, ▼, or ⚡) for a win!")  #intro
creditBalance = 50   #money
print("you have 50 credits!")   #original balance
#func
def completeSlotmachine():  #overall function
    global creditBalance
    while True:   #infinite loop
        spin = input("would you like to spin (standard / double / triple)?: ")   #user prompt
        if spin == "standard":
            creditBalance = creditBalance - 1
            slotOne = random.choice(symbols)  #slot assignment
            slotTwo = random.choice(symbols)
            slotThree = random.choice(symbols)
            fullSpin = slotOne + slotTwo + slotThree
            print("spinning slot one...")  #spindown
            time.sleep(1)
            print("spinning slot two...")
            time.sleep(1)
            print("spinning slot three...")
            time.sleep(1)
            if slotOne == "7" and slotTwo == "7" and slotThree == "7":  #jackpot outcome
                print(fullSpin)  #outcome
                print("jackpot! 50 credits!")
                creditBalance = creditBalance + 50
                creditCheck = "your current credit is " + str(creditBalance)  #balance update
                print(creditCheck)
            elif slotOne == slotTwo and slotTwo == slotThree and slotOne == slotThree:  #win outcome
                print(fullSpin)
                print("winner! 10 credits!")
                creditBalance = creditBalance + 10
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            elif slotOne == slotTwo or slotTwo == slotThree:
                creditBalance = creditBalance + 2                      #half-win chance
                print(fullSpin)
                print("half-win! 2 credits!")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            else:     #loss outcome
                print(fullSpin)
                print("bad spin...")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
        if spin == "double":
            creditBalance = creditBalance - 2  #wager deduction
            slotOne = random.choice(symbols)  #slot assignment
            slotTwo = random.choice(symbols)
            slotThree = random.choice(symbols)
            fullSpin = slotOne + slotTwo + slotThree
            print("spinning slot one...")  #spindown
            time.sleep(1)
            print("spinning slot two...")
            time.sleep(1)
            print("spinning slot three...")
            time.sleep(1)
            if slotOne == "7" and slotTwo == "7" and slotThree == "7":  #jackpot outcome
                print(fullSpin)  #outcome
                print("jackpot! 75 credits!")
                creditBalance = creditBalance + 75
                creditCheck = "your current credit is " + str(creditBalance)  #balance update
                print(creditCheck)
            elif slotOne == slotTwo and slotTwo == slotThree and slotOne == slotThree:  #win outcome
                print(fullSpin)
                print("winner! 13 credits!")
                creditBalance = creditBalance + 13
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            elif slotOne == slotTwo or slotTwo == slotThree:
                creditBalance = creditBalance + 3                      #half-win chance
                print(fullSpin)
                print("half-win! 3 credits!")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            else:     #loss outcome
                print(fullSpin)
                print("bad spin...")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
        if spin == "triple":
            creditBalance = creditBalance - 3  #wager deduction
            slotOne = random.choice(symbols)  #slot assignment
            slotTwo = random.choice(symbols)
            slotThree = random.choice(symbols)
            fullSpin = slotOne + slotTwo + slotThree
            print("spinning slot one...")  #spindown
            time.sleep(1)
            print("spinning slot two...")
            time.sleep(1)
            print("spinning slot three...")
            time.sleep(1)
            if slotOne == "7" and slotTwo == "7" and slotThree == "7":  #jackpot outcome
                print(fullSpin)  #outcome
                print("jackpot! 100 credits!")
                creditBalance = creditBalance + 100
                creditCheck = "your current credit is " + str(creditBalance)  #balance update
                print(creditCheck)
            elif slotOne == slotTwo and slotTwo == slotThree and slotOne == slotThree:  #win outcome
                print(fullSpin)
                print("winner! 15 credits!")
                creditBalance = creditBalance + 15
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            elif slotOne == slotTwo or slotTwo == slotThree:
                creditBalance = creditBalance + 5                      #half-win chance
                print(fullSpin)
                print("half-win! 5 credits!")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
            else:     #loss outcome
                print(fullSpin)
                print("bad spin...")
                creditCheck = "your current credit is " + str(creditBalance)
                print(creditCheck)
        if creditBalance == 0:
            print("you are out of funds!")   #broke
            break
        if spin == "no":   #user quit
            print("thanks for playing!")
            break  #loop stop
#main
completeSlotmachine()   #function call
