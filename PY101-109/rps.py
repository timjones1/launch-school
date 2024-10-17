import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

def display_winner(user_choice, comp_choice):

    if ((user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "scissors" and comp_choice == "paper")):
        prompt("You win!")
    elif ((user_choice == "rock" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("it's a tie!")

while True:

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)
    
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
