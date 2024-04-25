import random

random_number = random.randrange(1, 21)
number_of_guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    number_of_guesses +=1
    if guess == random_number:
        print("You win!")
        print(f"Number of guesses is: {number_of_guesses}")
        break
    elif guess > random_number:
        print("Your guess is too big") 
    elif guess < random_number:
        print("Your guess is too small")
       


