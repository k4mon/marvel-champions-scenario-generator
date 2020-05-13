from data.abstract import Villain, EncounterSet


class Rhino(Villain):
    name = "Rhino"
    preferred_encounter_set = EncounterSet.BOMB_SCARE

    def __init__(self, encounter_set=None):
        self.encounter_set = encounter_set or self.preferred_encounter_set


class Klaw(Villain):
    name = "Klaw"
    preferred_encounter_set = EncounterSet.MASTERS_OF_EVIL

    def __init__(self, encounter_set=None):
        self.encounter_set = encounter_set or self.preferred_encounter_set


class Ultron(Villain):
    name = "Ultron"
    preferred_encounter_set = EncounterSet.UNDER_ATTACK

    def __init__(self, encounter_set=None):
        self.encounter_set = encounter_set or self.preferred_encounter_set


class TheWreckingCrew(Villain):
    name = "The Wrecking Crew"
    preferred_encounter_set = None
    encounter_set = None

    def __init__(self, encounter_set=None):
        pass


VILLAINS = [Rhino, Klaw, Ultron, TheWreckingCrew]
