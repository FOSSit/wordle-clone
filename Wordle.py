import json
import random
from os import system, name
from time import sleep

with open("WordList.json", "r") as f:
    RAW_WORD_LIST = json.load(f)["words"]

WORD = random.choice(RAW_WORD_LIST)
GRID = [[" " for _ in range(5)] for _ in range(6)]
INCORRECT_WORDS = []

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
    1) A random 5 letter word is selected by the computer, the objective of the game is
       guess the word that is selected by 6 moves

    2) The user must enter valid 5 letter words every time they wish to make a guess

    3) Incorrect letters of the guess become visible in the 'Incorrect Letters' list

    4) Correct letters that are in the correct position are visible as 'UPPERCASE' characters

    5) Correct letters that are in the wrong position are visible as 'lowercase' characters
"""


def user_input() -> str:
    inp = input(
        "enter a 5 length word that you think may be the answer: ").capitalize()
    print(inp,)
    if len(inp) != 5:
        print(f"the entered word '{inp}' is not of length '5', try again\n")
        return user_input()

    if inp not in RAW_WORD_LIST:
        print(
            f"the entered word '{inp}' is not recognized by the game dictionary, try again\n")
        return user_input()

    return inp


def print_grid():
    grid = f"""
        | {GRID[0][0]} | {GRID[0][1]} | {GRID[0][2]} | {GRID[0][3]} | {GRID[0][4]} |
        | {GRID[1][0]} | {GRID[1][1]} | {GRID[1][2]} | {GRID[1][3]} | {GRID[1][4]} |
        | {GRID[2][0]} | {GRID[2][1]} | {GRID[2][2]} | {GRID[2][3]} | {GRID[2][4]} |
        | {GRID[3][0]} | {GRID[3][1]} | {GRID[3][2]} | {GRID[3][3]} | {GRID[3][4]} |
        | {GRID[4][0]} | {GRID[4][1]} | {GRID[4][2]} | {GRID[4][3]} | {GRID[4][4]} |
        | {GRID[5][0]} | {GRID[5][1]} | {GRID[5][2]} | {GRID[5][3]} | {GRID[5][4]} |
    """
    print(grid)


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def compare_characters(inp: str, TURNS: int):
    compare = list(zip(inp, WORD))
    for idx, char in enumerate(inp):
        if char.lower() in WORD.lower():
            GRID[TURNS][idx] = char.lower()
        else:
            INCORRECT_WORDS.append(char.lower())

    for idx, tup in enumerate(compare):
        if len(set(tup)) == 1:
            GRID[TURNS][idx] = tup[0].upper()


def game_logic():
    TURNS = 0
    while TURNS < 5:

        print(f"\nTURN NUMBER: {TURNS + 1}\n")

        print("\nINCORRECT_WORDS:")
        print(list(set(INCORRECT_WORDS)))
        print()

        print("\nCURRENT GRID")
        print_grid()

        print()
        inp = user_input()

        compare_characters(inp, TURNS)
        print(f"\nInputted word >>> {inp}")

        print("\nINCORRECT_WORDS:")
        print(list(set(INCORRECT_WORDS)))
        print()

        print("\nCURRENT GRID")
        print_grid()

        if inp == WORD:
            print(f"You guessed the word {WORD} in {TURNS + 1} turns")
            break

        play = input("enter [y/Y] to continue the game: ").lower()
        if play not in "yes":
            print("quitting game")
            break

        print("Continuing game")

        TURNS += 1
        sleep(0.5)
        clear_screen()

    else:
        print("You were not able to guess the word")
        print(f"The word was >>> {WORD}")
        print("Your current grid state is\n")
        print_grid()


def main():
    clear_screen()

    print(TITLE)
    print("\n\n\n")

    print("This is you grid")
    print_grid()
    print("\n", INSTRUCTIONS)

    play = input("enter [y/Y] to play the game: ").lower()
    if play not in "yes":
        print("quitting game")
        return
    sleep(0.5)
    clear_screen()

    game_logic()


main()
