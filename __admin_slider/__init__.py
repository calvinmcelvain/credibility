from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = '__admin_slider'
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
