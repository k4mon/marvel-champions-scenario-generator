from dataclasses import dataclass
from enum import Enum
from typing import List


class HeroAspect(Enum):
    AGGRESSION = "Aggression"
    JUSTICE = "Justice"
    LEADERSHIP = "Leadership"
    PROTECTION = "Protection"


class EncounterSet(Enum):
    BOMB_SCARE = "Bomb Scare"
    MASTERS_OF_EVIL = "Masters of Evil"
    UNDER_ATTACK = "Under Attack"
    LEGIONS_OF_HYDRA = "Legions of Hydra"
    THE_DOOMSDAY_CHAIR = "The Doomsday Chair"


@dataclass
class Hero:
    name: str
    aspect: HeroAspect
    preferred_aspect: HeroAspect


@dataclass
class Villain:
    name: str
    encounter_set: EncounterSet
    preferred_encounter_set: EncounterSet


@dataclass
class Game:
    heroes: List[Hero]
    villain: Villain
