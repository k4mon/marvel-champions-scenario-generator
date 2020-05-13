def print_game(game):
    print()
    print("You play as:")
    _print_heroes(game.heroes)
    print("Against:")
    _print_villain(game.villain)
    print()


def _print_heroes(heroes):
    for hero in heroes:
        print(f"\t{hero.name} with the {hero.aspect.value} aspect")


def _print_villain(villain):
    print(f"\t{villain.name} {_print_encounter_set(villain.encounter_set)}")


def _print_encounter_set(encounter_set):
    if encounter_set is not None:
        return f"with the {encounter_set.value} encounter set "
    return ""
