import argparse

from data.heroes import HEROES
from data.villains import VILLAINS
from presenter import print_game
from service.service import generate_game


def main(number_of_players, random_aspect, random_encounter_set):
    game = generate_game(
        HEROES, VILLAINS, number_of_players, random_aspect, random_encounter_set,
    )
    print_game(game)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a game of Marvel Champions.")
    parser.add_argument(
        "--number_of_players",
        type=int,
        help="The number of players in the game.",
        default=1,
        choices=range(1, 5),
        required=False,
    )
    parser.add_argument(
        "--random_aspect",
        action="store_true",
        help="Provide this flag if you want to randomize hero aspects.",
    )
    parser.add_argument(
        "--random_encounter_set",
        action="store_true",
        help="Provide this flag if you want to randomize the villain encounter set.",
    )

    main(**parser.parse_args().__dict__)
