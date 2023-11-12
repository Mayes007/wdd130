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
            print("\nYou decide to free the trapped animal. As you release it, the animal bounds away into the forest, leaving you with a sense of satisfaction.")
            print("With the animal saved, you continue down the path.")
            scenario_continue_path()
            break
        elif user_choice == "LEAVE":
            print("\nYou choose to leave the trapped animal and continue down the path.")
            print("The path leads you to a clearing where you discover a hidden stash of valuable gems.")
            print("Congratulations! You have found a hidden treasure. You win the game!")
            break
        else:
            print("Invalid choice. Please type 'FREE' or 'LEAVE'.\n")

def scenario_continue_path():
    print("\nAs you continue down the path, you encounter a series of challenges and adventures.")
    # Additional actions for this scenario can be added here.
