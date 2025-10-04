"""
Number Guessing Game Project
Author: Your Name
Description: A modular Python program where the user guesses a random
number between 1 and 10 within 5 attempts. Success shows a smiley image,
failure shows an angry image.
"""

import random
import tkinter as tk
from PIL import Image, ImageTk

# ------------------ Utility Functions ------------------ #

def generate_number():
    """Generate a random number between 1 and 10."""
    return random.randint(1, 10)

def get_user_guess():
    """Get user input and validate it."""
    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")

def show_image(path, title):
    """Display an image in a Tkinter window."""
    root = tk.Tk()
    root.title(title)
    img = Image.open(path)
    tk_img = ImageTk.PhotoImage(img)
    lbl = tk.Label(root, image=tk_img)
    lbl.pack()
    root.mainloop()

# ------------------ Main Game Logic ------------------ #

def play_game():
    """Run the number guessing game."""
    number = generate_number()
    attempts = 5
    print("🎮 Welcome to Number Guessing Game!")
    print("You have 5 attempts to guess the number between 1 and 10.\n")

    for attempt in range(1, attempts + 1):
        guess = get_user_guess()

        if guess == number:
            print(f"✅ Congratulations! You guessed it right in {attempt} attempt(s).")
            show_image("happy.png", "Success 🎉")
            return True
        elif guess < number:
            print("⬆️ Too low! Try again.")
        else:
            print("⬇️ Too high! Try again.")

        print(f"Attempts left: {attempts - attempt}\n")

    print(f"❌ Sorry! You used all attempts. The number was {number}.")
    show_image("angry.png", "Failure 😡")
    return False

# ------------------ Entry Point ------------------ #

if __name__ == "__main__":
    play_game()

