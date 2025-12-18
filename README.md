Battleship Game

#Input Format

Players enter ship coordinates in the format: LetterNumber (e.g., A1, D7, J10).

Multiple coordinates are separated by spaces.

Example for a 3-cell ship:

B1 B2 B3


Rows are letters A–J, columns are numbers 1–10.

The program automatically converts these coordinates to 0-based indices for internal processing.

#Ship Placement Validation

Correct size – the number of coordinates entered must match the ship size (e.g., 4 cells for the 4-cell ship).

Board boundaries – ships must be within a 10×10 board.

Straight line & consecutive cells – ships must be aligned horizontally or vertically, and the cells must be consecutive.

No touching – ships cannot touch each other, even diagonally.

If any rule is broken, the program asks the player to re-enter coordinates.

#Game State Update and Display

The game state is stored in data/game_state.csv, which is updated after each move.

Each entry includes: turn number, player move (coordinate + hit/miss), bot move (coordinate + hit/miss), and the state of all cells.

The 10×10 board is printed to the terminal for both players, using symbols:

X → hit

O → miss

. → unknown/empty cell

When a ship is destroyed, all surrounding cells are automatically marked as misses in the game state.

#Design Decisions / Trade-offs

Input format: Chose letter+number with spaces for simplicity and easy parsing.

Validation logic: Implemented reusable functions (coord_to_index, is_consecutive, mark_surroundings) in utils.py to avoid code duplication.

Game state storage: Used CSV for simplicity, making it easy to read and update the board.

Bot AI (optional): Implemented in a separate class for maintainability. If omitted, the bot shoots randomly.

Trade-off: For clarity, the game focuses on terminal interaction and does not include GUI. This makes testing and grading straightforward.
