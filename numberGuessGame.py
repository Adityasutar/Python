import random
print("Lets play this awesome number guessing game" , "\n")
lowerLimit = int(input("Set your Lower number Limit : "))
upperLimit = int(input("Set your Upper number Limit : "))
attempts = 2
i = 0
randomNum = random.randint(lowerLimit,upperLimit)
print("\n",f"Guess the number between {lowerLimit} and {upperLimit} : " ,"\n")
print(f"You have only {attempts} attempts to guess correct number ","\n")
while i < (attempts) :

    guessedNum = int(input("Enter your number : "))

    i += 1
    if randomNum > guessedNum :
        print("Guessed wrong number, hint ! : guess in Higher bound range " ,"\n")
    elif randomNum < guessedNum :
        print("Guessed wrong number, hint ! : guess in Lower bound range","\n")
    elif randomNum == guessedNum :
        print("\n","Viola !, you guessed the correct number")
        break

    # If all attempts are used up
    if i == attempts:
        print(f"Game over! The correct number was {randomNum}.")
    
    


