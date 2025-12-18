from src.ship_input import read_player_ships
from src.bot_generation import generate_bot_ships
from src.gameplay import (
    load_ships,
    empty_board,
    print_board,
    coord_to_index,
    apply_move,
    init_game_state,
    save_turn
)
import random

def all_ships_destroyed(ships, hits):
    all_cells = {cell for ship in ships for cell in ship}
    return all_cells.issubset(hits)


def main():
    read_player_ships()
    generate_bot_ships()

    player_ships = load_ships("data/player_ships.csv")
    bot_ships = load_ships("data/bot_ships.csv")

    player_view = empty_board()
    bot_view = empty_board()

    player_hits = set()
    bot_hits = set()

    init_game_state()
    turn = 1

    print("\nThe game has begun\n")

    while True:
        print_board(player_view, "Player field")
        move = input("\nYour turn (for example A5): ")

        r, c = coord_to_index(move)
        result = apply_move((r, c), bot_ships, player_view, player_hits)
        player_move_log = f"{move.upper()} {result}"

        if all_ships_destroyed(bot_ships, player_hits):
            save_turn(turn, player_move_log, "-", player_view, bot_view)
            print("\nYou won!")
            break

        while True:
            br = random.randint(0, 9)
            bc = random.randint(0, 9)
            if bot_view[br][bc] == ".":
                break

        bot_coord = (br, bc)
        bot_result = apply_move(bot_coord, player_ships, bot_view, bot_hits)
        bot_move_log = f"{chr(br + 65)}{bc + 1} {bot_result}"

        save_turn(turn, player_move_log, bot_move_log, player_view, bot_view)

        print_board(bot_view, "Bot field")

        if all_ships_destroyed(player_ships, bot_hits):
            print("\nThe bot wons!")
            break

        turn += 1


if __name__ == "__main__":
    main()