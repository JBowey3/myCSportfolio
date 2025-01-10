#james bowey
#name generator project
#init
print("welcome to Your Chicago Bears Player!")   #opening
print("Answer yes or no to the following questions to find out who your player is!!")
#functions
ans = input("Do you like football? (yes/no)")   #branch  1
if ans == "no" :
    ans = input("Do you procrastinate a lot? (yes/no)")
    if ans == "yes" :
        ans = input("Do you find exercise boring? (yes/no)")  #branch 2
        if ans == "yes":
            print("Your player is Nate Davis!")
        else:
            print("Your player is Patrick Scales!")
    else:
        ans = input("Do you see yourself as a leader? (yes/no)") #branch 3
        if ans == "yes":
            print("Your player is Kevin Byard!")
        else:
            print("Your player is Khalil Herbert!")
else:
    ans = input("Do you like to run? (yes/no)")  #branch 5
    if ans == "no" :
        ans = input("Are you outgoing? (yes/no)")
        if ans == "no":
            print("Your player is Andrew Billings!")   #branch 6
        else:
            print("Your player is Kyler Gordon!")
    else:
        ans = input("Do you have good eyesight? (yes/no)") #branch 7
        if ans == "no":
            print("Your player is DJ Moore!")
        else:                                           #branch 8 
            print("Your player is Caleb Williams!")
#main
