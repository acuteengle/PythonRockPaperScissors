import random

options = ["rock", "paper", "scissors"]

def randomSelection():
    index = random.randrange(0, len(options))
    return options[index]

player_score = 0
computer_score = 0
round_number = 1

while (True):
    print("--- ROUND " + str(round_number) + " ---")
    print("Please enter 'rock', 'paper', or 'scissors' (or 'exit' to quit)")
    print("Current Score: {Player Wins: %s,  Computer Wins: %s}" % (player_score, computer_score))
    player_answer = raw_input("What do you pick? ")
    print("")

    if (player_answer == "exit"):
        break
    elif (player_answer != "rock" and player_answer != "paper" and player_answer != "scissors"):
        print("Please enter a valid input\n")
        continue
    else:
        computer_answer = randomSelection()

        print("Player picks: %s" % (player_answer))
        print("Computer picks: %s" % (computer_answer))
        if (player_answer == computer_answer):
            print("IT'S A TIE!\n")
        elif ((player_answer == "paper" and computer_answer == "rock") or (player_answer == "rock" and computer_answer == "scissors") or (player_answer == "scissors" and computer_answer == "paper")):
            print("PLAYER WINS!\n")
            player_score += 1
        else:
            print("COMPUTER WINS!\n")
            computer_score += 1

        round_number += 1

print("Thanks for playing!")