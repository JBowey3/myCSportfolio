#james bowey
#12/10/24
#madlib project

#init
#below are predetermined variables that hold the story structure
sen1 = "You decided it was time to take a vacation to "
sen2 = "On the car drive there, a "
sen3 = " suddenly jumped into the road, and you swerved into a "
sen4 = "The "
sen5 = " was so "
sen6 = " that he chased you "
sen7 = " all the way back home! Vacation ruined."
#func
def MadLib():   #overall function calling the game
    print("welcome to this MadLib game!")  #next 3 lines is intro information
    print("you will be prompted to enter operatives such as an adjective or noun.")
    print("once all inputs are responded to, you'll receive your MadLib story!")
    place = input("enter any place: ")  #variables that store the details of the story (5 lines)
    animal = input("enter any animal: ")
    noun = input("enter any male celebrity: ")
    adj = input("enter any adjective: ")
    verb = input("enter any verb ending in -ly: ")
    story = sen1 + place + ". " + sen2 + animal + sen3 + noun + ". " + sen4 + noun + sen5 + adj + sen6 + verb + sen7
    #variable that combines all elements through string concatenation into a complete "Madlib"
    print(story)  #prints the full story for the user
#main
MadLib()
