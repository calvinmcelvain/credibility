from otree.api import *
from settings import grouping

doc = """
Experiment Wait-room: Sets group matrix and assigns player roles
"""


class C(BaseConstants):
    NAME_IN_URL = 'start'
    PLAYERS_PER_GROUP = grouping
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# Functions
def creating_session(subsession):
    # Storing group matrix
    subsession.session.vars['group_matrix'] = subsession.get_group_matrix()

    # Creating and storing player roles and setting stage 1 payoff to 0
    for player in subsession.get_players():
        player.participant.vars['PlayerID'] = 00
        player.participant.vars['STG1_payoff'] = cu(0)
        player.participant.vars['STG1_history'] = {}
        player.participant.vars['D1'] = cu(0)
        player.participant.vars['D2'] = cu(0)
        player.participant.vars['D3'] = cu(0)
        if player.id_in_group == 1:
            player.participant.vars['role'] = 'Advisor'
        else:
            player.participant.vars['role'] = 'Investor'


# PAGES
class ExperimentWaitRoom(WaitPage):
    title_text = 'Experiment will start soon'
    body_text = 'Please wait patiently'
    wait_for_all_groups = True


page_sequence = [ExperimentWaitRoom]
