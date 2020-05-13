from data.abstract import Hero, HeroAspect


class SpiderMan(Hero):
    name = "Spider-Man"
    preferred_aspect = HeroAspect.JUSTICE

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class IronMan(Hero):
    name = "Iron Man"
    preferred_aspect = HeroAspect.AGGRESSION

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class SheHulk(Hero):
    name = "She-Hulk"
    preferred_aspect = HeroAspect.AGGRESSION

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class BlackPanther(Hero):
    name = "Black Panther"
    preferred_aspect = HeroAspect.PROTECTION

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class CaptainMarvel(Hero):
    name = "Captain Marvel"
    preferred_aspect = HeroAspect.LEADERSHIP

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class Thor(Hero):
    name = "Thor"
    preferred_aspect = HeroAspect.AGGRESSION

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


class BlackWidow(Hero):
    name = "Black Widow"
    preferred_aspect = HeroAspect.JUSTICE

    def __init__(self, aspect=None):
        self.aspect = aspect or self.preferred_aspect


HEROES = [
    SpiderMan,
    IronMan,
    SheHulk,
    BlackPanther,
    CaptainMarvel,
    Thor,
    BlackWidow,
]
