import random

random_number = random.randrange(1, 21)
Number_of_guesses = 1

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == random_number:
        print("You win!")
        print(f"Number of guesses is: {Number_of_guesses}")
        break
    elif guess > random_number:
        print("Your guess is too big")
        Number_of_guesses +=1
    elif guess < random_number:
        print("Your guess is too small")
        Number_of_guesses +=1


