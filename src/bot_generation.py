import csv
import random

BOARD_SIZE = 10
REQUIRED_SHIPS = [4,3, 3, 2, 2, 2, 1, 1, 1, 1]


def touches_other_ship(board, cells):
    for r, c in cells:
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                    if board[nr][nc]:
                        return True
    return False

def generate_ships(size, board):
    while True:
        orientation = random.choice(["H","V"])

        if orientation == "H":
            row = random.randint(0,BOARD_SIZE-1)
            col = random.randint(0,BOARD_SIZE - size)
            cells = [(row, col + i) for i in range(size)]
        else:
            row = random.randint(0,BOARD_SIZE-size)
            col = random.randint(0,BOARD_SIZE-1)
            cells = [(row + i, col) for i in range(size)]
        
        if touches_other_ship(board,cells):
            continue
        
        return cells
    
def generate_bot_ships():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    ships = []
    
    for r,c in ship:
        board[r][c] = 1
    ships.append(ship)

    with open("data/bot_ships.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for ship in ships:
            writer.writerow([f"{r},{c}" for r, c in ship])

    return ships