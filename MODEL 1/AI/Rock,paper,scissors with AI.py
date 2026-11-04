import random
while True:
    user_input = input("What you chose: ").lower
    posible_actions = ["rock","paper","sissor"]

    computer_actions = random.choice(posible_actions)
    print("You chose",user_input,"The computer chose",computer_actions)

    if user_input == computer_actions:
        print("You both choosed the same,So it is a tie")
    elif user_input == "rock":
        if computer_actions == "sissor":
            print("Nice,You win 😄")
        else:
            print("Nice try buddy 😏")

    elif user_input == "paper":
        if computer_actions == "rock":
            print("Nice,You win 😄")
        else:
            print("Nice try buddy 😏")

    elif user_input == "sissor":
        if computer_actions == "paper":
            print("Nice,You win 😄")
        else:
            print("Nice try buddy 😏")
