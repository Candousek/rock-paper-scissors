"""
Rock Paper Scissors
"""

from math import floor
import random
import os

VALID_CHOICES = ["r", "p", "s"]
WIN_CONDITIONS = {
    "r": "s",
    "p": "r",
    "s": "p"
}
FULL_CHOICES_NAMES = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

def get_player_choice():
    """Functions asks player for a choice and returns it.

    Returns:
        str: Can be r (rock), p (paper) or s (scissors).
    """

    player_choice = input("""
Please choose what you want to play:
[R] Rock
[P] Paper
[S] Scissors

>> Your choice: """).lower()

    if player_choice not in VALID_CHOICES:
        clear_console()
        print("Invalid choice")
        return get_player_choice()

    return player_choice

def get_playmode():
    """Get a gamemode user wants to play.

    Returns:
        str: Can be AI or P2.
    """

    playmode_choice = input("""
Please select gamemode you want to play:
[1] Against an AI
[2] Against a friend (locally)

>> Your choice: """).lower()

    if playmode_choice not in ["1", "2"]:
        clear_console()
        print("Invalid choice")
        return get_playmode()

    return playmode_choice

def get_ai_choice():
    """Get AI's choice.

    Returns:
        str: Can be r (rock), p (paper) or s (scissors).
    """

    return random.choice(VALID_CHOICES)

def calculate_win(first_choice, second_choice):
    """Check if player wins.

    Args:
        first_choice (str): First players's choice.
        second_choice (str): Second player's choice.

    Returns:
        int: 1 if player wins, 0 if player loses, -1 if it's a draw.
    """

    if WIN_CONDITIONS[first_choice] == second_choice:
        return 1
    if WIN_CONDITIONS[second_choice] == first_choice:
        return 0
    return -1

def clear_console():
    """Clears the console.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

def print_result(result, is_ai):
    """Prints the result of the game.

    Args:
        result (int): Result of the game.
        is_ai (bool): True if it's an AI game, False if it's a P2 game.
    """

    if result == 1 and is_ai:
        print("\nYou won the game!")
    elif result == 0 and is_ai:
        print("\nYou lost!")
    elif result == 1 and not is_ai:
        print("\nPlayer 1 Won and Player 2 Lost!")
    elif result == 0 and not is_ai:
        print("\nPlayer 1 Lost and Player 2 Won!")
    else:
        print("\nIt's a draw!")

def main():
    """Main function for the whole game
    """

    terminal_size = os.get_terminal_size().columns
    clear_console()
    gamemode = get_playmode()
    clear_console()

    if gamemode == "1":
        while True:
            player_choice = get_player_choice()
            ai_choice = get_ai_choice()
            clear_console()
            print('\u2500' * floor(terminal_size/5))
            print(f"You chose: {FULL_CHOICES_NAMES[player_choice]}")
            print(f"AI chose: {FULL_CHOICES_NAMES[ai_choice]}")
            print_result(calculate_win(player_choice, ai_choice), True)
            print('\u2500' * floor(terminal_size/5))
    else:
        while True:
            print("FIRST PLAYER'S TURN")
            first_player_choice = get_player_choice()
            clear_console()
            print("SECOND PLAYER'S TURN")
            second_player_choice = get_player_choice()
            clear_console()
            print('\u2500' * floor(terminal_size/5))
            print(f"You chose: {FULL_CHOICES_NAMES[first_player_choice]}")
            print(f"AI chose: {FULL_CHOICES_NAMES[second_player_choice]}")
            print_result(calculate_win(first_player_choice, second_player_choice), False)
            print('\u2500' * floor(terminal_size/5))

if __name__ == "__main__":
    main()
