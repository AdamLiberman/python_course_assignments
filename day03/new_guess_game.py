import random

def com_number():
    random_number = random.randrange(1, 21)
    return random_number

def guessing(guess, random_number, number_of_guesses):
    if int(guess) == random_number:
        print("You win!")
        print(f"Number of guesses is: {number_of_guesses}")
        return True
    elif int(guess) > random_number:
        print("Your guess is too big") 
    elif int(guess) < random_number:
        print("Your guess is too small")
    
def game(random_number, number_of_guesses):
    is_game_over = False
    while not is_game_over:
        guess = input("Guess a number between 1 and 20: ")
        if guess=="x":
            break
        elif guess=="n":
            restart_game = input("Do you want to play a new game? ")
            if restart_game.lower() == "yes":
                number_of_guesses = 0
                random_number = com_number()
                continue
            elif restart_game.lower() == "no":
                continue
            else:    
                break
        elif guess == "s":
            print(f"the number is {random_number}")
            break
        else:
            number_of_guesses +=1
            is_game_over = guessing(guess, random_number, number_of_guesses)

def main():
    random_number = com_number()
    number_of_guesses = 0
    display = game(random_number, number_of_guesses)
    return display

main()