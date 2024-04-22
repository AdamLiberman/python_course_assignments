import random

random_number = random.randrange(1, 21)
Number_of_guesses = 1

while True:
    guess = input("guess a number: ")
    if int(guess) == random_number:
        print("You win!")
        print(f"Number of guesses is: {Number_of_guesses}")
        break
    elif int(guess) > random_number:
        print("Your guess is too big")
        Number_of_guesses +=1
    elif int(guess) < random_number:
        print("Your guess is too small")
        Number_of_guesses +=1


