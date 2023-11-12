import time

def scenario_dark_forest():
    print("You find yourself in a dark forest, surrounded by towering trees and an eerie silence.")
    print("You notice two items on the ground: a MATCH and a FLASHLIGHT. Which one do you want to pick up?\n")

    while True:
        user_choice = input("Type 'MATCH' or 'FLASHLIGHT': ").strip().upper()

        if user_choice == "MATCH":
            scenario_match()
            break
        elif user_choice == "FLASHLIGHT":
            scenario_flashlight()
            break
        else:
            print("Invalid choice. Please type 'MATCH' or 'FLASHLIGHT'.\n")

def scenario_match():
    print("\nYou pick up the match and strike it, briefly illuminating the forest.")
    print("Suddenly, you see a large grizzly bear approaching you. The match burns out.")
    print("Do you want to RUN or HIDE behind a tree?\n")

    while True:
        user_choice = input("Type 'RUN' or 'HIDE': ").strip().upper()

        if user_choice == "RUN":
            print("\nYou start running as fast as you can. The bear chases you, but you manage to escape and find a river.")
            scenario_run()
            break
        elif user_choice == "HIDE":
            print("\nYou quickly hide behind a tree, barely breathing.")
            print("The bear sniffs around and eventually leaves. You decide to follow a faint trail deeper into the forest.")
            scenario_hide()
            break
        else:
            print("Invalid choice. Please type 'RUN' or 'HIDE'.\n")

def scenario_flashlight():
    print("\nYou pick up the flashlight and turn it on. The pathway in front of you is lit up, but you hear a noise to the side.")
    print("Do you want to FOLLOW the path or LOOK in the trees for the source of the noise?\n")

    while True:
        user_choice = input("Type 'FOLLOW' or 'LOOK': ").strip().upper()

        if user_choice == "FOLLOW":
            print("\nYou decide to follow the path, hoping to find safety.")
            print("As you walk, you see a mysterious door partially hidden behind the trees.")
            scenario_follow()
            break
        elif user_choice == "LOOK":
            print("\nYou decide to look in the trees to investigate the noise.")
            print("You find a trapped animal. Do you want to FREE it or LEAVE it and continue?\n")
            scenario_look()
            break
        else:
            print("Invalid choice. Please type 'FOLLOW' or 'LOOK'.\n")

def scenario_run():
    print("\nYou reach the river and decide to FOLLOW it downstream.")
    # Additional actions for this scenario can be added here.

def scenario_hide():
    print("\nYou find a river and decide to FOLLOW it downstream.")
    # Additional actions for this scenario can be added here.

def scenario_follow():
    while True:
        user_choice = input("Type 'OPEN' or 'CONTINUE': ").strip().upper()

        if user_choice == "OPEN":
            print("\nYou cautiously open the door and find a hidden treasure chest!")
            print("Congratulations! You have found the treasure and won the game.")
            break
        elif user_choice == "CONTINUE":
            print("\nYou choose to continue down the path, leaving the mysterious door behind.")
            print("You find a river and decide to FOLLOW it downstream.")
            scenario_run()
            break
        else:
            print("Invalid choice. Please type 'OPEN' or 'CONTINUE'.\n")

def scenario_look():
    while True:
        user_choice = input("Type 'FREE' or 'LEAVE': ").strip().upper()

        if user_choice == "FREE":
            print("\nYou free the trapped animal, and it runs away gratefully.")
            print("You find a river and decide to FOLLOW it downstream.")
            scenario_run()
            break
        elif user_choice == "LEAVE":
            print("\nYou choose to leave the trapped animal and continue down the path.")
            print("You find a river and decide to FOLLOW it downstream.")
            scenario_run()
            break
        else:
            print("Invalid choice. Please type 'FREE' or 'LEAVE'.\n")

# Start the game by calling the first scenario
scenario_dark_forest()

def level_1():
    print("You find yourself lost in the Enchanted Forest.")
    print("You see two paths ahead, one leading deeper into the forest and the other leading back the way you came.")
    
    while True:
        choice = input("What do you want to do? (GO DEEPER INTO THE FOREST / TURN BACK AND GO THE OTHER WAY): ").strip().upper()
        
        if choice == "GO DEEPER INTO THE FOREST":
            level_2()
            break
        elif choice == "TURN BACK AND GO THE OTHER WAY":
            print("You return to where you started.")
            break
        else:
            print("Please choose a valid option.")

def level_2():
    print("You venture deeper into the forest and suddenly encounter a group of magical creatures.")
    print("They offer you a choice of two magical items - a GLOWING AMULET or a MYSTERIOUS POTION.")
    
    while True:
        choice = input("What do you want to choose? (GLOWING AMULET / MYSTERIOUS POTION): ").strip().upper()
        
        if choice == "GLOWING AMULET":
            print("The amulet illuminates your path and leads you to Level 3.")
            level_3()
            break
        elif choice == "MYSTERIOUS POTION":
            print("You become invisible but start feeling strange. You have another choice.")
            level_2a()
            break
        else:
            print("Please choose a valid option.")

def level_2a():
    print("You need to make another choice about what to do with the MYSTERIOUS POTION.")
    
    while True:
        choice = input("What do you want to do with the potion? (DRINK / DISCARD): ").strip().upper()
        
        if choice == "DRINK":
            print("The potion makes you invisible, but you experience side effects.")
            print("You return to Level 1.")
            level_1()
            break
        elif choice == "DISCARD":
            print("You wisely discard the potion and continue your adventure.")
            level_3()
            break
        else:
            print("Please choose a valid option.")

def level_3():
    print("With the help of the glowing amulet, you find yourself facing the ancient Enchanted Tree.")
    print("It presents you with three challenges. Choose your challenge:")
    
    while True:
        choice = input("What challenge do you want to take? (RIDDLE CHALLENGE / STRENGTH CHALLENGE / COURAGE CHALLENGE): ").strip().upper()
        
