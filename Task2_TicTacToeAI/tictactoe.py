import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

board = [""] * 9
buttons = []

def check_winner(b):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        a, b1, c = combo

        if board[a] == board[b1] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def minimax(board_state, is_maximizing):
    result = check_winner(board_state)

    if result == "O":
        return 1

    elif result == "X":
        return -1

    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "O"
                score = minimax(board_state, False)
                board_state[i] = ""
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "X"
                score = minimax(board_state, True)
                board_state[i] = ""
                best_score = min(score, best_score)

        return best_score


def ai_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == "":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"
        buttons[move].config(text="O")

    result = check_winner(board)

    if result:
        end_game(result)


def player_move(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X")

        result = check_winner(board)

        if result:
            end_game(result)
            return

        ai_move()


def end_game(result):
    if result == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")

    else:
        messagebox.showinfo("Game Over", f"{result} Wins!")

    reset_game()


def reset_game():
    global board

    board = [""] * 9

    for button in buttons:
        button.config(text="")


for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    button.grid(row=i//3, column=i%3)

    buttons.append(button)


root.mainloop()