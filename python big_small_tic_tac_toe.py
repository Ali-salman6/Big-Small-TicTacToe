import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from PIL import Image, ImageTk


# ------------------ Main Menu Window ------------------

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Big-Small Tic Tac Toe - Main Menu")
        self.root.geometry("450x500")
        self.mode = tk.StringVar(value="PvP")
        self.board_size = tk.IntVar(value=3)

        # Background image
        img = Image.open("C:\\Users\\pc\\Desktop\\BigSmall.png")
        img = img.resize((450, 500), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(img)
        self.bg_label = tk.Label(root, image=self.tk_image)
        self.bg_label.place(x=0, y=0)

        # Game mode selection
        tk.Label(self.root, text="Select Game Mode:", font=("Helvetica", 14), bg="#ffffff").place(relx=0.5, rely=0.055, anchor="n")
        tk.Radiobutton(self.root, text="Player vs Player", variable=self.mode, value="PvP",
                       font=("Helvetica", 12), bg="#ffffff").place(relx=0.45, rely=0.13, anchor="ne")
        tk.Radiobutton(self.root, text="Player vs Computer", variable=self.mode, value="PvC",
                       font=("Helvetica", 12), bg="#ffffff").place(relx=0.9, rely=0.13, anchor="ne")

        # Board size selection
        tk.Label(self.root, text="Select Board Size:", font=("Helvetica", 14), bg="#ffffff").place(relx=0.1, rely=1, anchor="sw")
        size_options = [3,4,5,6,7,8,9,10]
        tk.OptionMenu(self.root, self.board_size, *size_options).place(relx=0.5, rely=1, anchor="sw")

        # Button
        tk.Button(self.root, text="Start Game", foreground="white", background="deepskyblue",
                  command=self.start_game, font=("Helvetica", 12)).place(relx=0.7, rely=1, anchor="sw")

    def start_game(self):
        self.root.withdraw()
        GameWindow(self.root, self.mode.get(), self.board_size.get())


# ------------------ Game Window ------------------

class GameWindow:
    def __init__(self, main_root, mode, board_size):
        self.mode = mode
        self.board_size = board_size
        self.main_root = main_root

        self.window = tk.Toplevel()
        self.window.title("Tic Tac Toe Game")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.score = {"X": 0, "O": 0, "Draw": 0}
        self.current_player = "X"
        self.big_moves = {"X": 2, "O": 2}

        top_frame = tk.Frame(self.window)
        top_frame.pack(pady=5)

        self.score_label = tk.Label(top_frame, text=self.get_score_text(), font=("Helvetica", 12))
        self.score_label.pack(side="left", padx=10)

        self.turn_label = tk.Label(top_frame, text=f"Turn: {self.current_player}", font=("Helvetica", 12, "bold"))
        self.turn_label.pack(side="left", padx=10)

        tk.Button(top_frame, text="Change Board Size", command=self.change_board_size, font=("Helvetica", 10)).pack(side="left", padx=5)
        tk.Button(top_frame, text="Back to Main Menu", command=self.back_to_menu, font=("Helvetica", 10)).pack(side="left", padx=5)

        size_frame = tk.Frame(self.window)
        size_frame.pack(pady=5)
        tk.Label(size_frame, text="Select Piece Size:", font=("Helvetica", 12)).pack(side="left", padx=5)
        self.selected_size = tk.IntVar(value=1)
        self.small_rb = tk.Radiobutton(size_frame, text="Small", variable=self.selected_size, value=1, font=("Helvetica", 12))
        self.small_rb.pack(side="left", padx=5)
        self.big_rb = tk.Radiobutton(size_frame, text="Big", variable=self.selected_size, value=2, font=("Helvetica", 12))
        self.big_rb.pack(side="left", padx=5)

        self.update_piece_size_options()

        self.canvas = tk.Canvas(self.window, width=600, height=600, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.create_board()

    def get_score_text(self):
        return f"Score - X: {self.score['X']}   O: {self.score['O']}   Draws: {self.score['Draw']}"

    def create_board(self):
        self.cell_size = 600 // self.board_size
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.canvas.delete("all")

        for i in range(1, self.board_size):
            self.canvas.create_line(0, i * self.cell_size, 600, i * self.cell_size, width=2)
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, 600, width=2)

        self.current_player = "X"
        self.big_moves = {"X": 2, "O": 2}
        self.update_piece_size_options()
        self.update_turn_label()

    def on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if row >= self.board_size or col >= self.board_size:
            return

        new_size = self.selected_size.get()
        if new_size == 2 and self.big_moves[self.current_player] <= 0:
            messagebox.showinfo("Info", "No big moves left! Using small piece instead.")
            new_size = 1
            self.selected_size.set(1)

        cell = self.board[row][col]
        if cell is None:
            if new_size == 2:
                self.big_moves[self.current_player] -= 1
            self.board[row][col] = (self.current_player, new_size)
        else:
            if cell[0] == self.current_player:
                return
            if new_size > cell[1]:
                if new_size == 2:
                    self.big_moves[self.current_player] -= 1
                self.board[row][col] = (self.current_player, new_size)
            else:
                messagebox.showinfo("Invalid Move", "New piece is not larger than opponent's!")
                return

        self.draw_piece(row, col)

        if self.check_win(self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.score[self.current_player] += 1
            self.update_score()
            self.create_board()
            return
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.score["Draw"] += 1
            self.update_score()
            self.create_board()
            return

        self.switch_player()
        self.update_piece_size_options()
        self.update_turn_label()

        if self.mode == "PvC" and self.current_player == "O":
            self.window.after(500, self.computer_move)

    def draw_piece(self, row, col):
        x0 = col * self.cell_size + 10
        y0 = row * self.cell_size + 10
        x1 = (col + 1) * self.cell_size - 10
        y1 = (row + 1) * self.cell_size - 10
        player, size = self.board[row][col]

        if player == "O" and size == 2:
            self.canvas.create_oval(x0, y0, x1, y1, outline="blue", width=4)
        elif player == "X" and size == 2:
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="red", width=4)
        else:
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=player, font=("Helvetica", 24))

    def check_win(self, player):
        def has_three_consecutive(lst):
            count = 0
            for cell in lst:
                if cell and cell[0] == player:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 0
            return False

        bs = self.board_size

        # Check rows and columns
        for i in range(bs):
            if has_three_consecutive([self.board[i][j] for j in range(bs)]):
                return True
            if has_three_consecutive([self.board[j][i] for j in range(bs)]):
                return True

        # Check diagonals
        for d in range(bs - 2):
            for i in range(bs - 2 - d):
                # Top-left to bottom-right
                if has_three_consecutive([self.board[i + k][k + d] for k in range(bs - d - i)]):
                    return True
                if has_three_consecutive([self.board[k + d][i + k] for k in range(bs - d - i)]):
                    return True
                # Top-right to bottom-left
                if has_three_consecutive([self.board[i + k][bs - 1 - (k + d)] for k in range(bs - d - i)]):
                    return True
                if has_three_consecutive([self.board[k + d][bs - 1 - (i + k)] for k in range(bs - d - i)]):
                    return True

        return False

    def check_draw(self):
        return all(self.board[i][j] is not None for i in range(self.board_size) for j in range(self.board_size))

    def computer_move(self):
        free_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] is None]
        if not free_cells:
            return
        row, col = random.choice(free_cells)
        new_size = 2 if self.big_moves[self.current_player] > 0 and random.random() < 0.3 else 1
        if new_size == 2:
            self.big_moves[self.current_player] -= 1
        self.board[row][col] = (self.current_player, new_size)
        self.draw_piece(row, col)

        if self.check_win(self.current_player):
            messagebox.showinfo("Game Over", f"Computer ({self.current_player}) wins!")
            self.score[self.current_player] += 1
            self.update_score()
            self.create_board()
            return
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.score["Draw"] += 1
            self.update_score()
            self.create_board()
            return

        self.switch_player()
        self.update_piece_size_options()
        self.update_turn_label()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def update_turn_label(self):
        self.turn_label.config(text=f"Turn: {self.current_player}")

    def update_score(self):
        self.score_label.config(text=self.get_score_text())

    def update_piece_size_options(self):
        if self.big_moves[self.current_player] <= 0:
            self.big_rb.config(state="disabled")
            self.selected_size.set(1)
        else:
            self.big_rb.config(state="normal")

    def change_board_size(self):
        new_size = simpledialog.askinteger("Board Size", "Enter new board size (3 to 10):", minvalue=3, maxvalue=10)
        if new_size and new_size != self.board_size:
            self.board_size = new_size
            self.create_board()

    def back_to_menu(self):
        self.window.destroy()
        self.main_root.deiconify()

    def on_closing(self):
        self.back_to_menu()

# ------------------ Start Application ------------------

if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()
