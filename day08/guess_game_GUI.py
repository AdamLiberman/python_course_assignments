import tkinter as tk
import random
from tkinter import messagebox

class guessing_game(tk.Tk):
    def __init__(self):
        self.random_number = random.randrange(1, 21)
        self.number_of_guesses = 0
        super().__init__()

        self.title("Guess Game")

        self.label = tk.Label(self, text="Guess a number between 1 and 20!")
        self.label.pack()

        self.get_guess = tk.Entry(self)
        self.get_guess.pack(fill= "both")  

        self.guess_button = tk.Button(self, text="Guess", command= self.guessing)
        self.guess_button.pack(fill= "both")

        self.show_answer_button = tk.Button(self, text="Show Answer", command= self.show_answer)
        self.show_answer_button.pack(fill= "both")

        self.restart_button = tk.Button(self, text="Restart", command= self.draw_number)
        self.restart_button.pack(fill= "both")

        self.exit_button = tk.Button(self, text="Exit", command= self.close)
        self.exit_button.pack(fill= "both")

    def close(self):
        print("closing")
        self.quit()

    def show_answer(self):
        messagebox.showinfo(title = "Show answer", message = f"The number is {self.random_number}")

    def draw_number(self):
        self.random_number = random.randrange(1, 21)
        self.number_of_guesses = 0

    def guessing(self):
        guess = self.get_guess.get()
        try:
            self.number_of_guesses +=1
            if int(guess) == self.random_number:
                print("You win!")
                print(f"Number of guesses is: {self.number_of_guesses}")
            elif int(guess) > self.random_number:
                print("Your guess is too big") 
            elif int(guess) < self.random_number:
                print("Your guess is too small") 
        except ValueError:
            print("Please guess a number")

def main():

    app = guessing_game()
    app.mainloop()

main()