import json
import random
from os import system, name
from time import sleep

# Define ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open("WordList.json", "r") as f:
    RAW_WORD_LIST = json.load(f)["words"]

WORD = random.choice(RAW_WORD_LIST)
GRID = [[" " for _ in range(5)] for _ in range(6)]
INCORRECT_WORDS = []

TITLE = f"""
{Colors.HEADER}
     __       __   ______   _______   _______   __        ________         ______   __         ______   __    __  ________
    /  |  _  /  | /      \\ /       \\ /       \\ /  |      /        |       /      \\ /  |       /      \\ /  \\  /  |/        |
    $$ | / \\ $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |$$ |      $$$$$$$$/       /$$$$$$  |$$ |      /$$$$$$  |$$  \\ $$ |$$$$$$$$/
    $$ |/$  \\$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ |      $$ |__          $$ |  $$/ $$ |      $$ |  $$ |$$$  \\$$ |$$ |__
    $$ /$$$  $$ |$$ |  $$ |$$    $$< $$ |  $$ |$$ |      $$    |         $$ |      $$ |      $$ |  $$ |$$$$  $$ |$$    |
    $$ $$/$$ $$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |      $$$$$/          $$ |   __ $$ |      $$ |  $$ |$$ $$ $$ |$$$$$/
    $$$$/  $$$$ |$$ \\__$$ |$$ |  $$ |$$ |__$$ |$$ |_____ $$ |_____       $$ \\__/  |$$ |_____ $$ \\__$$ |$$ |$$$$ |$$ |_____
    $$$/    $$$ |$$    $$/ $$ |  $$ |$$    $$/ $$       |$$       |      $$    $$/ $$       |$$    $$/ $$ | $$$ |$$       |
    $$/      $$/  $$$$$$/  $$/   $$/ $$$$$$$/  $$$$$$$$/ $$$$$$$$/        $$$$$$/  $$$$$$$$/  $$$$$$/  $$/   $$/ $$$$$$$$/
{Colors.ENDC}
"""

INSTRUCTIONS = f"""
{Colors.OKBLUE}
INSTRUCTIONS:
    1) A random 5 letter word is selected by the computer, the objective of the game is
       guess the word that is selected by 6 moves

    2) The user must enter valid 5 letter words every time they wish to make a guess

    3) Incorrect letters of the guess become visible in the 'Incorrect Letters' list

    4) Correct letters that are in the correct position are visible as 'UPPERCASE' characters

    5) Correct letters that are in the wrong position are visible as 'lowercase' characters
{Colors.ENDC}
"""


def user_input() -> str:
    inp = input(
        "enter a 5 length word that you think may be the answer: ").capitalize()
    print(inp, WORD)
    if len(inp) != 5:
        print(f"{Colors.FAIL}the entered word '{inp}' is not of length '5', try again\n{Colors.ENDC}")
        return user_input()

    if inp not in RAW_WORD_LIST:
        print(
            f"{Colors.FAIL}the entered word '{inp}' is not recognized by the game dictionary, try again\n{Colors.ENDC}")
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

        print(f"\n{Colors.OKGREEN}TURN NUMBER: {TURNS + 1}\n{Colors.ENDC}")

        print(f"\n{Colors.WARNING}INCORRECT_WORDS:{Colors.ENDC}")
        print(list(set(INCORRECT_WORDS)))
        print()

        print(f"\n{Colors.OKBLUE}CURRENT GRID{Colors.ENDC}")
        print_grid()

        print()
        inp = user_input()

        compare_characters(inp, TURNS)
        print(f"\n{Colors.OKGREEN}Inputted word >>> {inp}{Colors.ENDC}")

        print(f"\n{Colors.WARNING}INCORRECT_WORDS:{Colors.ENDC}")
        print(list(set(INCORRECT_WORDS)))
        print()

        print(f"\n{Colors.OKBLUE}CURRENT GRID{Colors.ENDC}")
        print_grid()

        if inp == WORD:
            print(f"{Colors.OKGREEN}You guessed the word {WORD} in {TURNS + 1} turns{Colors.ENDC}")
            break

        play = input("enter [y/Y] to continue the game: ").lower()
        if play not in "yes":
            print(f"{Colors.FAIL}quitting game{Colors.ENDC}")
            break

        print(f"{Colors.OKGREEN}Continuing game{Colors.ENDC}")

        TURNS += 1
        sleep(0.5)
        clear_screen()

    else:
        print(f"{Colors.FAIL}You were not able to guess the word{Colors.ENDC}")
        print(f"{Colors.WARNING}The word was >>> {WORD}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Your current grid state is\n{Colors.ENDC}")
        print_grid()


def main():
    clear_screen()

    print(TITLE)
    print("\n\n\n")

    print(f"{Colors.OKGREEN}This is your grid{Colors.ENDC}")

    print_grid()
    print("\n", INSTRUCTIONS)

    play = input("enter [y/Y] to play the game: ").lower()
    if play not in "yes":
        print(f"{Colors.FAIL}quitting game{Colors.ENDC}")

        return
    sleep(0.5)
    clear_screen()

    game_logic()


main()
