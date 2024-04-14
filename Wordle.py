# Import necessary libraries
import json
import random
from os import system, name
from time import sleep

# Load the word list
with open("WordList.json", "r") as f:
    RAW_WORD_LIST = json.load(f)["words"]

# Choose a random word
WORD = random.choice(RAW_WORD_LIST)
GRID = [[" " for _ in range(5)] for _ in range(6)]
INCORRECT_WORDS = []

# Define title and instructions
TITLE = r"""
     __       __   ______   _______   _______   __        ________         ______   __         ______   __    __  ________
    /  |  _  /  | /      \ /       \ /       \ /  |      /        |       /      \ /  |       /      \ /  \  /  |/        |
    $$ | / \ $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |$$ |      $$$$$$$$/       /$$$$$$  |$$ |      /$$$$$$  |$$  \ $$ |$$$$$$$$/
    $$ |/$  \$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ |      $$ |__          $$ |  $$/ $$ |      $$ |  $$ |$$$  \$$ |$$ |__
    $$ /$$$  $$ |$$ |  $$ |$$    $$< $$ |  $$ |$$ |      $$    |         $$ |      $$ |      $$ |  $$ |$$$$  $$ |$$    |
    $$ $$/$$ $$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |      $$$$$/          $$ |   __ $$ |      $$ |  $$ |$$ $$ $$ |$$$$$/
    $$$$/  $$$$ |$$ \__$$ |$$ |  $$ |$$ |__$$ |$$ |_____ $$ |_____       $$ \__/  |$$ |_____ $$ \__$$ |$$ |$$$$ |$$ |_____
    $$$/    $$$ |$$    $$/ $$ |  $$ |$$    $$/ $$       |$$       |      $$    $$/ $$       |$$    $$/ $$ | $$$ |$$       |
    $$/      $$/  $$$$$$/  $$/   $$/ $$$$$$$/  $$$$$$$$/ $$$$$$$$/        $$$$$$/  $$$$$$$$/  $$$$$$/  $$/   $$/ $$$$$$$$/
"""

INSTRUCTIONS = """
INSTRUCTIONS:
    1) A random 5-letter word is selected by the computer. The objective of the game is to guess the word within 6 moves.

    2) The user must enter valid 5-letter words each time they make a guess.

    3) Incorrect letters of the guess become visible in the 'Incorrect Letters' list.

    4) Correct letters that are in the correct position are visible as 'UPPERCASE' characters.

    5) Correct letters that are in the wrong position are visible as 'lowercase' characters.
"""

# Define color codes
color_codes = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}
def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
# Helper functions to print colored text and grids
def print_colored(text, color):
    print(color_codes[color] + text + color_codes["reset"])

def print_grid():
    colored_grid = "\n"
    for row in GRID:
        colored_grid += " | ".join(row)
        colored_grid += " |\n"
    print_colored(colored_grid, "cyan")

# Continue the rest of your functions using the print_colored and print_grid functions
# Use the helper functions to print the title and instructions with colors as well

# For example, in the game_logic function, when you want to print the grid or instructions, use print_grid() and print_colored
def user_input() -> str:
    inp = input(
        "enter a 5 length word that you think may be the answer: ").capitalize()
    print(inp, WORD)
    if len(inp) != 5:
        print(f"the entered word '{inp}' is not of length '5', try again\n")
        return user_input()

    if inp not in RAW_WORD_LIST:
        print(
            f"the entered word '{inp}' is not recognized by the game dictionary, try again\n")
        return user_input()

    return inp

def game_logic():
    TURNS = 0
    while TURNS < 6:
        print_colored(f"\nTURN NUMBER: {TURNS + 1}\n", "green")
        
        print_colored("\nINCORRECT WORDS:", "red")
        print(list(set(INCORRECT_WORDS)))
        
        print("\nCURRENT GRID")
        print_grid()
        
        inp = user_input()
        
        compare_characters(inp, TURNS)
        print_colored(f"\nInputted word >>> {inp}\n", "blue")
        
        print_colored("\nINCORRECT WORDS:", "red")
        print(list(set(INCORRECT_WORDS)))
        
        print("\nCURRENT GRID")
        print_grid()
        
        if inp == WORD:
            print_colored(f"You guessed the word {WORD} in {TURNS + 1} turns!", "green")
            break
        
        play = input("Enter [y/Y] to continue the game: ").lower()
        if play not in "yes":
            print("Quitting game")
            break
        
        print("Continuing game")
        
        TURNS += 1
        sleep(0.5)
        clear_screen()
    
    else:
        print_colored("You were not able to guess the word.", "red")
        print(f"The word was >>> {WORD}")
        print_colored("Your current grid state is:", "magenta")
        print_grid()

def main():
    clear_screen()
    
    print_colored(TITLE, "magenta")
    print("\n\n\n")
    
    print_colored("This is your grid", "blue")
    print_grid()
    print("\n")
    print_colored(INSTRUCTIONS, "cyan")
    
    play = input("Enter [y/Y] to play the game: ").lower()
    if play not in "yes":
        print_colored("Quitting game", "red")
        return
    sleep(0.5)
    clear_screen()
    
    game_logic()

main()
