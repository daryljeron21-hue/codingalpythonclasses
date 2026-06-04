import random
playing = True
num = str(random.randint(0,9))
print("A random number is chosen between 0 to 9 you need to guess it on time")
#while playing:
guess = 5
if num == guess:
    print("You won the number is correct")
else:
    print("No you lost because the number is",num)

#Activity2
import random
while True:
    user_input = "rock"
    posible_actions = ["rock","paper","sissor"]

    computer_actions = random.choice(posible_actions)
    print("You chose",user_input,"The computer chose",computer_actions)

    if user_input == computer_actions:
        print("You both choosed the same,So it is a tie")
    elif user_input == "rock":
        if computer_actions == "sissor":
            print("You win")
        else:
            print("You lose")

    elif user_input == "paper":
        if computer_actions == "rock":
            print("You win")
        else:
            print("You lose")

    elif user_input == "sissor":
        if computer_actions == "paper":
            print("You win")
        else:
            print("You lose")
