import tkinter as tk

board_size = 15
cell_size = 40
padding = 20

board = [[0] * board_size for _ in range(board_size)]
players = {
    1: "흑돌",
    2: "백돌"
}
current_player = 1

def make_move(row, col):
    if board[row][col] == 0:
        board[row][col] = current_player
        canvas.create_oval(
            padding + col * cell_size - cell_size // 2, padding + row * cell_size - cell_size // 2,
            padding + col * cell_size + cell_size // 2, padding + row * cell_size + cell_size // 2,
            fill="black" if current_player == 1 else "white"
        )
        if check_winner(row, col):
            canvas.unbind("<Button-1>")
            winner = players[current_player]
            canvas.create_text(
                padding + board_size * cell_size // 2, padding // 2,
                text=f"축하합니다! {winner}이 이겼습니다.",
                font=("Arial", 16), fill="red"
            )
        else:
            switch_player()

def check_winner(row, col):
    player = board[row][col]

    # 가로 방향 체크
    count = 1
    for i in range(1, 5):
        if col - i >= 0 and board[row][col - i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if col + i < board_size and board[row][col + i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 세로 방향 체크
    count = 1
    for i in range(1, 5):
        if row - i >= 0 and board[row - i][col] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row + i < board_size and board[row + i][col] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 대각선 방향 체크 (왼쪽 위에서 오른쪽 아래로)
    count = 1
    for i in range(1, 5):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row + i < board_size and col + i < board_size and board[row + i][col + i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    # 대각선 방향 체크 (오른쪽 위에서 왼쪽 아래로)
    count = 1
    for i in range(1, 5):
        if row - i >= 0 and col + i < board_size and board[row - i][col + i] == player:
            count += 1
        else:
            break
    for i in range(1, 5):
        if row + i < board_size and col - i >= 0 and board[row + i][col - i] == player:
            count += 1
        else:
            break
    if count >= 5:
        return True

    return False

def switch_player():
    global current_player
    current_player = 2 if current_player == 1 else 1

window = tk.Tk()
window.title("오목 게임")

canvas = tk.Canvas(
    window, width=board_size * cell_size + 2 * padding,
    height=board_size * cell_size + 2 * padding
)
canvas.pack()

for i in range(board_size):
    canvas.create_line(
        padding, padding + i * cell_size,
        padding + (board_size - 1) * cell_size, padding + i * cell_size
    )
    canvas.create_line(
        padding + i * cell_size, padding,
        padding + i * cell_size, padding + (board_size - 1) * cell_size
    )

canvas.bind("<Button-1>", lambda event: make_move((event.y - padding + cell_size // 2) // cell_size, (event.x - padding + cell_size // 2) // cell_size))

window.mainloop()
