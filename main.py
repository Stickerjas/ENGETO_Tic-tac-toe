"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomáš Jasný
email: tomas.jasny@seznam.cz
"""

def main():
    """
    Main function to run the Tic-Tac-Toe game. Runs the game loop.
    """
    game_board = [" ", " ", " ",
                   " ", " ", " ",
                    " ", " ", " "]
    current_player = "X"
    winner = None
    game_on = True
    separator = "========================================"
    oneline_separator = "----------------------------------------"


    print("Welcome to Tic Tac Toe")
    print(separator)
    print("""GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row""")
    print(separator)
    print("Let's start the game")
    print(oneline_separator)

    def print_board(board):
        """
        Prints the current state of the game board.

        Args:
            board (list): The game board as a list of 9 elements.
        """
        board_separator = "+---+---+---+"
        print(board_separator)
        print(f"|{board[0]:^3}|{board[1]:^3}|{board[2]:^3}|")
        print(board_separator)
        print(f"|{board[3]:^3}|{board[4]:^3}|{board[5]:^3}|")
        print(board_separator)
        print(f"|{board[6]:^3}|{board[7]:^3}|{board[8]:^3}|")
        print(board_separator)

    def player_input(board):
        """
        Prompts the current player to pick a number and updates the board accordingly.

        Args:
            board (list): The current game board.

        Ensures input is valid (type integer in range of 1–9, and space on board is empty).
        """
        while True:
            try:
                number = int(input(f"Player {current_player.lower()} | Please enter your move number:"))
                if number < 1 or number > 9:
                    print("Wrong range of picked number. Please try it again.")
                elif number >= 1 and number <= 9 and board[number-1] == " ":
                    board[number-1] = current_player
                    break
                else:
                    print("Another player is already at that spot. Please try it again.")
            except ValueError:
                print("Wrong entry. Please try it again.")

    def check_win_condition(board):
        """
        Checks if the current board has a winning condition.

        Args:
            board (list): The current game board.

        Returns:
            bool: True = winner, otherwise False.
        """
        nonlocal winner
        if board[0] == board[1] == board[2] and board[1] != " ":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != " ":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != " ":
            winner = board[6]
            return True
        elif board[0] == board[3] == board[6] and board[0] != " ":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != " ":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != " ":
            winner = board[2]
            return True
        elif board[0] == board[4] == board[8] and board[0] != " ":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != " ":
            winner = board[2]
            return True
        else:
            return False


    def change_player():
        """
        Switches the current player from X to O or vice versa.
        """
        nonlocal current_player
        if current_player =="X":
            current_player = "O"
        else:
            current_player = "X"

    def check_tie(board):
        """
        Checks if the board is full and declares a tie if there is no winner.

        Args:
            board (list): The current game board.
        """
        nonlocal game_on
        if " " not in board:
            print_board(board)
            print("It is a tie!")
            game_on = False

    def check_win(board):
        """
        Checks for a win and ends the game if one of players has won.

        Args:
            board (list): The current game board.
        """
        nonlocal game_on
        if check_win_condition(board):
            print_board(board)
            print(separator)
            print(f"Congratulations, the player {winner.lower()} WON!")
            print(separator)
            game_on = False

    while game_on:
        print_board(game_board)
        print(separator)
        player_input(game_board)
        print(separator)
        check_win(game_board)
        check_tie(game_board)
        change_player()

if __name__ == "__main__":
    main()