# 🧠 Big Small Tic Tac Toe Using Python GUI 

Welcome to **Big-Small Tic Tac Toe**, a fun and strategic twist on the classic Tic Tac Toe game! 
Built using Python and Tkinter, this version adds a new dimension: **piece size**. 
Each player has limited "big" pieces that can **override smaller opponent pieces**, making every move count.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9c9d59a1-8331-4ff4-a04e-32178518a37a" width="600" height="600">
</p>



## 🎮 Game Features

- **Game Modes**:  
  - Player vs Player (PvP)  
  - Player vs Computer (PvC)

- **Custom Board Sizes**: Choose between 3x3 to 10x10 grids.

- **Piece Types**:
  - Small piece (unlimited)
  - Big piece (limited to 2 per player per game)

- **Overwrite Mechanism**: Big pieces can **overwrite smaller opponent pieces**.

- **Win Condition**: Connect **3 same-player pieces in a row**, either horizontally, vertically, or diagonally.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  ```bash
  pip install pillow

## 🎮 Running the Game

- Make sure BigSmall.png (background image) exists at the correct path, or modify the path in the code.
- Run the script:
  ```bash
  python big_small_tic_tac_toe.py

## 📁 Project Structure
- big_small_tic_tac_toe.py   # Main application code
- BigSmall.png               # Background image (optional aesthetic)
- README.md                  # You're reading it!

## 🧩 Code Breakdown

### 1. `MainMenu` Class
- Initializes the main menu window using `tkinter`.
- Displays:
  - 🎮 Game mode selection: `Player vs Player` or `Player vs Computer`.
  - 🔢 Board size selector (3x3 to 10x10).
  - 🚀 "Start Game" button to launch the game.
- Loads a background image to enhance UI.
- On clicking "Start Game", it opens the `GameWindow`.

---

### 2. `GameWindow` Class
- Manages all gameplay logic and in-game UI.
- Initializes:
  - 🧩 Score display and turn tracker.
  - 🎛️ Radio buttons to choose piece size (`Small` or `Big`).
  - 🎨 Drawing canvas for the game board.
- Handles:
  - 👆 Mouse click input to place/move pieces.
  - 🔄 Switching player turns.
  - 🤖 Computer logic (if `PvC` mode is selected).
  - 🛠️ Dynamic board resizing and returning to main menu.

---

### 3. Piece Placement Logic
- Each board cell stores a tuple: `(player_symbol, size)`.
- Piece sizes:
  - `1` = Small piece (can be overwritten by size 2).
  - `2` = Big piece (can overwrite smaller enemy pieces).
- Each player gets **2 big pieces** per round.
- Rules:
  - A player can place a piece on an empty cell.
  - A **big** piece can **overwrite a small enemy piece**.
  - Cannot overwrite your own piece or equal/larger enemy piece.

---

### 4. Computer Moves (`PvC` Mode)
- If the mode is `Player vs Computer`, "O" is controlled by the AI.
- The AI:
  - Randomly selects an available cell.
  - Uses a big piece with a 30% probability (if available).
  - Waits 0.5 seconds before moving to simulate real turn-taking.

---

### 5. Victory Conditions (`check_win()` method)
- A player wins if they align **3 matching pieces** horizontally, vertically, or diagonally.
- The `check_win()` method:
  - Iterates through all rows, columns, and diagonals.
  - Uses a helper method to check for **three consecutive** pieces of the current player.

---

### 6. Draw Condition
- The game is declared a draw if **all cells are filled** and no winner is found.

---

### 7. Utility Methods
- `draw_piece()` – Renders the player's piece on the canvas based on size and type.
- `update_score()` – Refreshes the score label.
- `update_piece_size_options()` – Enables/disables the "Big" size option based on remaining big pieces.
- `change_board_size()` – Lets players resize the board during the game.
- `back_to_menu()` – Returns to the main menu without quitting the app.

---

## 🛠️ Future Enhancements

- Smarter AI with basic strategy.
- Sound effects and animations.
- Multiplayer over network.




