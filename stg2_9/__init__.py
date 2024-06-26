from otree.api import *
from settings import INSTRUCTIONS_TIME

doc = """
Stage 2 Scenario 4 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_9'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = INSTRUCTIONS_TIME

    # Decision Payoff dictionaries
    pb_payoff_scenario1 = {
        1: {1: 0, 2: 0, 3: 0, 4: 0},
        3: {1: 400, 2: 400, 3: 400, 4: 400},
    }
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 400, 4: 400},
        3: {1: 0, 2: 0, 3: 400, 4: 400},
    }
    pa_payoff = {
        1: {0: 0, 1: 100, 2: 200, 3: 300, 4: 400},
        3: {0: 0, 1: 100, 2: 200, 3: 300, 4: 400}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    pass


# PAGES
# Conditional Base Page
class BaseReadyPage(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pb_table': C.pb_payoff_scenario1}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P2(BaseReadyPage):
    pass


class P3(BaseReadyPage):
    pass


class P4(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3, P4]
