from otree.api import *
from settings import GROUPING

doc = """
Experiment wait-room: 
Sets group matrix and assigns player roles
"""


class C(BaseConstants):
    NAME_IN_URL = 'start'
    PLAYERS_PER_GROUP = GROUPING
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

    for player in subsession.get_players():
        # Setting initial values for participant variables
        player.participant.vars['stage_1_payoff'] = cu(0)
        player.participant.vars['stage_1_history'] = {}
        player.participant.vars['scenario_1_history'] = {}
        player.participant.vars['scenario_2_history'] = {}
        player.participant.vars['scenario_3_history'] = {}
        
        # Creating and storing player roles
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
