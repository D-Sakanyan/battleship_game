import csv

BOARD_SIZE = 10
REQUIRED_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def coord_to_index(coordinates):
    coordinates = coordinates.strip().upper()

    row_letter = coordinates[0]
    col_number = coordinates[1:]

    row = ord(row_letter) - ord('A')
    col = int(col_number) - 1

    return(row,col)

def is_inside_board(cells):
    return all(0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE for c,r in cells)

def is_straight_line(cells):
    rows = {r for r, _ in cells}
    cols = {c for _, c in cells}
    return len(rows) == 1 or len(cols) == 1

def is_consecutive(cells):
    cells = sorted(cells)
    rows = [r for r,_ in cells]
    cols = [c for _,c in cells]

    if len(set(rows)) == 1:
        return all(cols[i]+1 == cols[i+1] for i in range(len(cols)-1))
    if len(set(cols)) == 1:
        return all(rows[i]+1 == rows[i+1] for i in range(len(rows)-1))
    return False

def ship_borders(board,cells):
    for r,c in cells:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                    if board[nr][nc] == 1:
                        return True
    return False

def read_player_ships():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    ships = []
    
    for size in REQUIRED_SHIPS:
        while True:
            user = input(f"Input coordinates of size {size}: ").strip()
            parts = user.split()

            if len(parts) != size:
                print(f"Wrong count of coordinates. Need {size}")
                continue

            cells = [coord_to_index(p) for p in parts]

            if not is_inside_board(cells):
                print("Out of board")
                continue
            if size > 1 and not is_straight_line(cells):
                print("Ship is not straight")
                continue
            if size > 1 and not is_consecutive(cells):
                print("Coordinates is not consecutive")
                continue
            if ship_borders(board, cells):
                print("This place is not empty")
                continue
            
            for r,c in cells:
                board[r][c] = 1
            ships.append(cells)
            break

    with open("data/player_ships.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for ship in ships:
            writer.writerow([f"{r},{c}" for r, c in ship])
    return ships