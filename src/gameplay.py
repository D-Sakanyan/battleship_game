import csv

BOARD_SIZE = 10

def load_ships(path):
    ships = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            ship = []
            for cell in row:
                r,c = map(int,cell.split(","))
                ship.append((r,c))
            ships.append(ship)
    return ships

def empty_board():
    return [["."] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def print_board(board,title):
    print(f"\n{title}")
    print(" A B C D E F G H I J")
    for i, row in enumerate(board):
        print(f"{i+1:2}",end=" ")
        print(" ".join(row))

def board_to_string(board):
    return "".join("".join(row) for row in board)

def coord_to_index(coord):
    coord = coord.upper().strip()
    r = ord(coord[0] - ord('A'))
    c = int(coord[1:] - 1)
    return r,c

def mark_surroundings(board, ship_cells):
    for r,c in ship_cells:
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                    if board[nr][nc] == ".":
                        board[nr][nc] = "O"

def check_destroyed(ship, hits):
    return all(cell in hits for cell in ship)


def apply_move(coord, enemy_ships, view_board, hits):
    r, c = coord

    for ship in enemy_ships:
        if (r, c) in ship:
            view_board[r][c] = "X"
            hits.add((r, c))

            if check_destroyed(ship, hits):
                mark_surroundings(view_board, ship)
                return "hit (destroyed)"

            return "hit"

    view_board[r][c] = "O"
    return "miss"


def init_game_state():
    with open("data/game_state.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "turn",
            "player_move",
            "bot_move",
            "player_board",
            "bot_board"
        ])


def save_turn(turn, player_move, bot_move, player_board, bot_board):
    with open("data/game_state.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            turn,
            player_move,
            bot_move,
            board_to_string(player_board),
            board_to_string(bot_board)
        ])
