from otree.api import *


doc = """
For slider exmaple in Stage 2 (Page 6)
"""


class C(BaseConstants):
    NAME_IN_URL = '_slider'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Slider(Page):
    pass


page_sequence = [Slider]
