#james bowey
#11/21/24
#pokemon game

#init
import random
#global variables
pokemon_level = 0
pokemon_name = "Charmander"

#func
def pokemon_game():    #overall function calling the entire game (final)
    print("welcome to pokemon evolution")   #welcome statement
while True:
    if pokemon_level >= 10:     #lvl 10+ possible evolutions threshold (includes bonus random power evol)
        outcomes = random.randint(1,2)
        if outcomes == 1:
	        pokemon_name = "Charizard"
        if outcomes == 2:
            pokemon_name = "Mega-Charizard"
    elif pokemon_level >= 5:     #lvl 5-10 possible evolution threshold (only this range)
        pokemon_name = "Charmeleon"
    print("choose today's activity: ")   #activity/menu section (4 user prompts)
    print("""1. train
2. gym battle
3. rest (display info)
4. quit""")
    option = int(input("(1-4) select option: "))
    if option == 1:     #training setup (includes action statement and level increase)
        print(pokemon_name + " shot 10 fireballs and gained 1 level")
        pokemon_level = pokemon_level + 1
        print(pokemon_name + " is now level " + str(pokemon_level))
    if option == 2:     #battle setup (includes random battle outcome, updated level display)
        outcome = random.randint(1,2)
        if outcome == 1:
            print(pokemon_name + " lost the gym battle and did not gain any levels")
            print(pokemon_name + " is now level " + str(pokemon_level))
        if outcome == 2:
            print(pokemon_name + " won the gym battle and gained 2 levels")
            pokemon_level = pokemon_level + 2
            print(pokemon_name + " is now level " + str(pokemon_level))
    if option == 3:    #rest/idle setup (action statement and level, evolution updates)
        print(pokemon_name + " took a nap")
        print(pokemon_name + " is currently level " + str(pokemon_level))
        print("this pokemon's evolution is " + pokemon_name)
    if option == 4:   #quit the game/full halt (goes back to welcome/opening screen)
        break

#main
pokemon_game()
