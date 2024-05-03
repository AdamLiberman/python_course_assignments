import random

def com_number():
    random_number = random.randrange(1, 21)
    return random_number

def guessing(random_number, number_of_guesses):
    while True:
        guess = input("Guess a number between 1 and 20: ")
        number_of_guesses +=1
        if guess=="x":
            break
        if guess=="n":
            restart_game = input("Do you want to play a new game? ")
            if restart_game.lower() == "yes":
                number_of_guesses = 0
                random_number = com_number()
                continue
            if restart_game.lower() == "no" or "x":
                break
        if guess=="s":
            print(f"the number is {random_number}")
            break
        elif int(guess) == random_number:
            print("You win!")
            print(f"Number of guesses is: {number_of_guesses}")
            break
        elif int(guess) > random_number:
            print("Your guess is too big") 
        elif int(guess) < random_number:
            print("Your guess is too small")

def main():
    random_number = com_number()
    number_of_guesses = 0
    display = guessing(random_number, number_of_guesses)
    return display

main()