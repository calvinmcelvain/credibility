from otree.api import *
from settings import INSTRUCTIONS_TIME, SKIP

doc = """
Scenario 3 instructions app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_5'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = INSTRUCTIONS_TIME
    
    # Defining "Advisor" role
    advisor_ROLE = 'Advisor'
    
    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

    # Decision payoff dictionaries
    stg2_s3_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 0, 4: 0},
        'High': {1: 0, 2: 0, 3: 400, 4: 400},
    }
    stg2_s3_advisor_payoffs = {
        'Low': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400},
        'High': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    # Not passed to data export
    all_players_ready = models.IntegerField(initial=0)
    
    # Group treatment field
    treatment = models.StringField()


class Player(BasePlayer):
    pass


# PAGES
# Conditional base page
class BaseReadyPage(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        '''
        Making instruction pages conditional on all players in session clicking 'Continue'.
        See javascript for participant side.
        '''
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) if SKIP == False else 1
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P1(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


class P2(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


class P3(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3]
