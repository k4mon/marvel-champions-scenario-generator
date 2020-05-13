from random import choice, sample

from data.abstract import HeroAspect, EncounterSet, Game


def generate_game(
    heroes,
    villains,
    number_of_players=1,
    random_aspect=False,
    random_encounter_set=False,
):
    hero_list = sample(heroes, number_of_players)
    heroes = [
        hero(choice(list(HeroAspect)) if random_aspect else None) for hero in hero_list
    ]
    villain = choice(villains)(choice(list(EncounterSet)) if random_encounter_set else None)
    return Game(heroes=heroes, villain=villain)
