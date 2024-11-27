"""
Author: Paul Sommers
Date written: 11/27/2024
Assignment: Exercise 9-5 - GUI-Based Guess-the-Number Game
Short Desc: This program creates a GUI-based game where the computer guesses a number between 1 and 100, and the user provides hints (Too small, Too large, Correct). 
            The game resets when the user clicks "New game".
"""

from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    """A GUI-based guessing game where the computer guesses the user's number."""
    
    def __init__(self):
        """Initialize the frame and instance variables."""
        EasyFrame.__init__(self, title="Guessing Game")
        
        # Create game variables
        self.low = 1
        self.high = 100
        self.guess = random.randint(self.low, self.high)
        
        # Create and add GUI parts
        self.label = self.addLabel(text=f"Is the number {self.guess}?", 
                                 row=0, column=0, columnspan=4)
        
        # Add buttons
        self.tooSmallBtn = self.addButton(text="Too small", row=1, column=0,
                                         command=self.too_small)
        self.tooLargeBtn = self.addButton(text="Too large", row=1, column=1,
                                         command=self.too_large)
        self.correctBtn = self.addButton(text="Correct", row=1, column=2,
                                       command=self.correct)
        self.newGameBtn = self.addButton(text="New game", row=1, column=3,
                                       command=self.new_game)
    
    def too_small(self):
        """Handle Too small button click."""
        self.low = self.guess + 1
        if self.low <= self.high:
            self.guess = random.randint(self.low, self.high)
            self.label["text"] = f"Is the number {self.guess}?"
        else:
            self.label["text"] = "You must have made a mistake!"
            self.disable_game_buttons()
    
    def too_large(self):
        """Handle Too large button click."""
        self.high = self.guess - 1
        if self.low <= self.high:
            self.guess = random.randint(self.low, self.high)
            self.label["text"] = f"Is the number {self.guess}?"
        else:
            self.label["text"] = "You must have made a mistake!"
            self.disable_game_buttons()
    
    def correct(self):
        """Handle Correct button click."""
        self.label["text"] = "Awesome!  I'm a Winner! Thanks for playing!"
        self.disable_game_buttons()
    
    def new_game(self):
        """Reset the game."""
        self.low = 1
        self.high = 100
        self.guess = random.randint(self.low, self.high)
        self.label["text"] = f"Is the number {self.guess}?"
        self.enable_game_buttons()
    
    def disable_game_buttons(self):
        """Disable the game buttons."""
        self.tooSmallBtn["state"] = "disabled"
        self.tooLargeBtn["state"] = "disabled"
        self.correctBtn["state"] = "disabled"
    
    def enable_game_buttons(self):
        """Enable the game buttons."""
        self.tooSmallBtn["state"] = "normal"
        self.tooLargeBtn["state"] = "normal"
        self.correctBtn["state"] = "normal"

# Start the game
def main():
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()