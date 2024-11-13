import random
print("\n","Hello there, lets play this awesome game called ","\n" "ROCK PAPER SCISSOR")
print("Rules : Rock breaks Scissor, Paper covers Rock and Scissor cuts Paper" , "\n")
attempts = 3
actions = ['rock','paper','scissor']
i = 0
while i < (attempts):
    i +=1
    computer_action = random.choice(actions)
    user_input = input("Choose your action against computer ('rock','paper','scissor') : ").lower()
    
    if user_input == 'rock':
        if computer_action == 'scissor':
            print("Viola ! , you won !")
            break
        elif computer_action == 'paper':
            print("You lost, paper covers rock, retry..")

    elif user_input == 'paper':
        if computer_action == 'rock':
            print("Viola ! , you won !")
            break
        elif computer_action == 'scissor':
            print("You lost, scissor cuts paper, retry..")

    elif user_input == 'scissor':
        if computer_action == 'paper':
            print("Viola ! , you won !")
            break
        elif computer_action == 'rock':
            print("You lost, scissor gets crushed by rock, retry..")
            





