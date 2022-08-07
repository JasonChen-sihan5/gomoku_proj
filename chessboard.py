import tkinter as board

PIECE_SIZE = 10
piece_color = "black"
#board
root = board.TK()
root.title("Gomoku Game")
root.geometry("760x560")

#chess pieces
frames = board.Canvas(root, width=220, height=50)
frames.grid(row = 0, column = 1)
frames.create_oval(100 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_pieces"))