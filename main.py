import random

rock_ascii = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper_ascii = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors_ascii = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to the Rock, Paper, Scissors game!")
confirm = input("Press Enter to continue or type (help) for the rules: ").lower()

if confirm == "help":
    print(""" 
******** RULES ********
1) You choose, and the computer chooses.
2) Rock smashes Scissors → Rock wins.
3) Scissors cut Paper → Scissors wins.
4) Paper covers Rock → Paper wins.
""")

# User input
choice = input("Enter your choice (rock, paper, scissors): ").lower()

if choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice.")
else:
    if choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif choice == "paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")

    # Computer choice
    comp_choice = random.choice(["rock", "paper", "scissors"])
    if comp_choice == "rock":
        print(f"Computer chose:\n{rock_ascii}")
    elif comp_choice == "paper":
        print(f"Computer chose:\n{paper_ascii}")
    else:
        print(f"Computer chose:\n{scissors_ascii}")

    # Determine winner
    if choice == comp_choice:
        print("It's a tie!")
    elif (
        (choice == "rock" and comp_choice == "scissors") or
        (choice == "paper" and comp_choice == "rock") or
        (choice == "scissors" and comp_choice == "paper")
    ):
        print(f"You win! {choice.capitalize()} beats {comp_choice}.")
    else:
        print(f"You lose! {comp_choice.capitalize()} beats {choice}.")
