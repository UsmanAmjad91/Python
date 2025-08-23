# Muhammad Usman Amjad

import random
from typing import List, Optional, Tuple

Board = List[str]

def create_board() -> Board:
    return [" "]*9

def print_board(board: Board):
    # Display both symbols and position indices for clarity
    positions = [str(i+1) for i in range(9)]
    display = []
    for i in range(9):
        cell = board[i] if board[i] != " " else positions[i]
        display.append(cell)
    print()
    print(f" {display[0]} | {display[1]} | {display[2]}")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]}")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]}")
    print()

WIN_PATTERNS = [
    (0,1,2),(3,4,5),(6,7,8), # rows
    (0,3,6),(1,4,7),(2,5,8), # cols
    (0,4,8),(2,4,6)          # diagonals
]

def winner(board: Board) -> Optional[str]:
    for a,b,c in WIN_PATTERNS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board: Board) -> bool:
    return all(cell != " " for cell in board)

def available_moves(board: Board) -> List[int]:
    return [i for i,cell in enumerate(board) if cell == " "]

def make_move(board: Board, idx: int, player: str):
    board[idx] = player

def undo_move(board: Board, idx: int):
    board[idx] = " "

def minimax(board: Board, maximizing: bool, ai: str, human: str, alpha: float, beta: float, depth: int=0) -> Tuple[int, Optional[int]]:
    # Terminal check
    w = winner(board)
    if w == ai:
        return 10 - depth, None
    elif w == human:
        return depth - 10, None
    elif is_full(board):
        return 0, None

    best_move = None
    if maximizing:
        best_score = -float('inf')
        for move in available_moves(board):
            make_move(board, move, ai)
            score, _ = minimax(board, False, ai, human, alpha, beta, depth+1)
            undo_move(board, move)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = float('inf')
        for move in available_moves(board):
            make_move(board, move, human)
            score, _ = minimax(board, True, ai, human, alpha, beta, depth+1)
            undo_move(board, move)
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

def ai_move(board: Board, difficulty: str, ai: str, human: str) -> int:
    moves = available_moves(board)
    if difficulty.lower() == "easy":
        return random.choice(moves)
    # Hard: use minimax
    _, move = minimax(board, True, ai, human, -float('inf'), float('inf'))
    return move

def get_player_move(board: Board) -> int:
    while True:
        choice = input("Enter a position (1-9): ").strip()
        if not choice.isdigit():
            print("Please enter a number 1-9.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx > 8:
            print("Out of range. Choose 1-9.")
            continue
        if board[idx] != " ":
            print("That spot is taken. Try again.")
            continue
        return idx

def play_two_player():
    board = create_board()
    current = "X"
    print_board(board)
    while True:
        print(f"Player {current}'s turn.")
        idx = get_player_move(board)
        make_move(board, idx, current)
        print_board(board)
        w = winner(board)
        if w:
            print(f"Player {w} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"

def play_single_player():
    board = create_board()
    human = ""
    while human not in ["X","O"]:
        human = input("Choose your symbol (X goes first) [X/O]: ").upper().strip()
    ai = "O" if human == "X" else "X"
    difficulty = ""
    while difficulty.lower() not in ["easy","hard"]:
        difficulty = input("Choose difficulty [Easy/Hard]: ").strip()
    current = "X"
    print_board(board)
    while True:
        if current == human:
            print("Your turn.")
            idx = get_player_move(board)
        else:
            print(f"Computer ({difficulty.title()}) is thinking...")
            idx = ai_move(board, difficulty, ai, human)
        make_move(board, idx, current)
        print_board(board)
        w = winner(board)
        if w:
            if w == human:
                print("You win! Congratulations.")
            else:
                print("Computer wins.")
            break
        if is_full(board):
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"

def main():
    print("=== Ultimate Tic-Tac-Toe (Classic 3x3) ===")
    while True:
        mode = input("Select mode: [1] Single Player  [2] Two Player  [Q] Quit: ").strip().lower()
        if mode == "1":
            play_single_player()
        elif mode == "2":
            play_two_player()
        elif mode == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")
            continue
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
