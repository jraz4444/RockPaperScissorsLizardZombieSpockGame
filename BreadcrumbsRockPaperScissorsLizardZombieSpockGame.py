#import
import random

#Go over the rules of the game
print("These are the rules of the game for the rock,scissors,paper,lizard,zombie,spock")
print("Rock defeats Scissors")
print("Scissors defeats Paper")
print("Paper defeats Rock")
print("The same shapes end as a tie.")
print("Rock crushes Lizard")
print("Spock beats Scissors")
print("Lizard beats Spock")
print("Rock beats Zombie")
print("Scissors beats Zombie")
print("Lizard beats paper")
print("Paper beats Spock")
print("Spock beats Rock")
print("Zombie beats paper")
print("Zombie beats Lizard")

#list of the different choices
choices = ["rock", "scissors", "paper", "lizard", "spock", "zombie"]

# The player chooses the first option
choice = input("What is your first choice? ").lower()

# The computer randomly chooses the second option
choice_2 = random.choice(choices)
print(f"Computer chose: {choice_2}")

# Determine the winner
if choice == "rock" and choice_2 == "scissors":
    print(str(choice) + " won!")
elif choice == "scissors" and choice_2 == "rock":
    print(choice_2 + " won!")
elif choice == "scissors" and choice_2 == "paper":
    print(choice + " won!")
elif choice == "paper" and choice_2 == "scissors":
    print(choice_2 + " won!")
elif choice == "paper" and choice_2 == "rock":
    print(choice + " won!")
elif choice == "rock" and choice_2 == "paper":
    print(choice_2 + " won!")
elif choice == "rock" and choice_2 == "lizard":
    print(choice + " won!")
elif choice == "lizard" and choice_2 == "rock":
    print(choice_2 + " won!")
elif choice == "spock" and choice_2 == "scissors":
    print(choice + " won!")
elif choice == "scissors" and choice_2 == "spock":
    print(choice_2 + " won!")
elif choice == "lizard" and choice_2 == "spock":
    print(choice + " won!")
elif choice == "spock" and choice_2 == "lizard":
    print(choice_2 + " won!")
elif choice == "rock" and choice_2 == "zombie":
    print(choice + " won!")
elif choice == "zombie" and choice_2 == "rock":
    print(choice_2 + " won!")
elif choice == "scissors" and choice_2 == "zombie":
    print(choice + " won!")
elif choice == "zombie" and choice_2 == "scissors":
    print(choice_2 + " won!")
elif choice == "lizard" and choice_2 == "paper":
    print(choice + " won!")
elif choice == "paper" and choice_2 == "lizard":
    print(choice_2 + " won!")
elif choice == "paper" and choice_2 == "spock":
    print(choice + " won!")
elif choice == "spock" and choice_2 == "paper":
    print(choice_2 + " won!")
elif choice == "spock" and choice_2 == "rock":
    print(choice + " won!")
elif choice == "rock" and choice_2 == "spock":
    print(choice_2 + " won!")
elif choice == "zombie" and choice_2 == "paper":
    print(choice + " won!")
elif choice == "paper" and choice_2 == "zombie":
    print(choice_2 + " won!")
elif choice == "zombie" and choice_2 == "lizard":
    print(choice + " won!")
elif choice == "lizard" and choice_2 == "zombie":
    print(choice_2 + " won!")
elif choice == choice_2:
    print("Tie!")
