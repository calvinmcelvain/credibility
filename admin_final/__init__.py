from otree.api import *


doc = """
Final Confirmation Screen for admin overhead
"""


class C(BaseConstants):
    NAME_IN_URL = 'admin_final'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    # Decision payoff dictionaries
    stg2_s3_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 0, 4: 0},
        'High': {1: 0, 2: 0, 3: 400, 4: 400},
    }
    stg2_s3_advisor_payoffs = {
        'Low': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400},
        'High': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400}
    }
    
    # Previous investor payoff dictionaries
    stg2_s1_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 0, 4: 0},
        'High': {1: 400, 2: 400, 3: 400, 4: 400},
    }
    stg2_s2_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 400, 4: 400},
        'High': {1: 0, 2: 0, 3: 400, 4: 400},
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class FinalConfirmation(Page):
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing all investor payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs, 's2_investor_table': C.stg2_s2_investor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


page_sequence = [FinalConfirmation]
