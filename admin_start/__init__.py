from otree.api import *
doc = """
Experiment wait-room for admin: 
Almost perfect replicate of 'start' app but only has 1 person in a group (needed for proper start as admin)
"""


class C(BaseConstants):
    NAME_IN_URL = 'admin_start'
    PLAYERS_PER_GROUP = None
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
        player.participant.vars['role'] = 'Advisor'


# PAGES
class ExperimentWaitRoom(WaitPage):
    title_text = ''
    body_text = ''
    wait_for_all_groups = True


page_sequence = [ExperimentWaitRoom]