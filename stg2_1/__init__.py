from otree.api import *
from settings import INSTRUCTIONS_TIME, SKIP
import random as r

doc = """
Stage 2 & scenario 1 instructions app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = INSTRUCTIONS_TIME
    
    # Defining "Advisor" role
    advisor_ROLE = 'Advisor'
    
    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

    # Decision payoff dictionaries
    stg2_s1_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 0, 4: 0},
        'High': {1: 400, 2: 400, 3: 400, 4: 400},
    }
    stg2_s1_advisor_payoffs = {
        'Low': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400},
        'High': {0: 0, 1: 100, 2: 200, 3: 300, 4: 400}
    }
    
    # Sample payoff dictionaries
    investor_payoffs_sample = {
        'Low': {1: 400, 2: 0, 3: 400, 4: 0},
        'High': {1: 0, 2: 400, 3: 0, 4: 400},
    }
    advisor_payoffs_sample = {
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
    # Sample decision fields
    advisor_low_advice = models.StringField(blank=False)
    advisor_high_advice = models.StringField(blank=False)
    investor_minimum_endowment = models.IntegerField(blank=False, min=0, max=400)
    
    # Sample page variables
    draws = models.LongStringField()
    random_investors = models.LongStringField()
    
    def get_random_investors(self):
        '''
        Function to generate 20 sample total other investors between 1 and 3
        '''
        investors = [r.randint(1,3) for x in range(20)]
        r.shuffle(investors) 
        return investors


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
    pass


class P2(BaseReadyPage):
    pass


class P3(BaseReadyPage):
    pass


class P4(BaseReadyPage):
    pass


class P5(BaseReadyPage):
    pass


class P6(BaseReadyPage):
    pass


class P7(BaseReadyPage):
    pass


class P8(BaseReadyPage):
    pass


class P9(BaseReadyPage):
    pass


class P10(BaseReadyPage):
    pass


class P11(BaseReadyPage):
    form_model = 'player'
    form_fields = ['advisor_low_advice', 'advisor_high_advice']
    
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing the sample player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.advisor_payoffs_sample, 'investor_table': C.investor_payoffs_sample}


class P11WaitPage(WaitPage):
    body_text = 'Waiting until everyone has clicked continue'
    

class P12(BaseReadyPage):
    form_model = 'player'
    form_fields = ['investor_minimum_endowment']
    
    @staticmethod
    def vars_for_template(player):
        '''
        Passing the sample player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.advisor_payoffs_sample, 'investor_table': C.investor_payoffs_sample}


class P12WaitPage(WaitPage):
    body_text = 'Waiting until everyone has clicked continue'
    

class P13(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        '''
        Passing sample draws, total other investors, investor/advisor payoffs to HTML
        '''
        # Creating 20 draws of 250
        # Only random part is the amount of investors
        draws = [250] * 20
        investors_rand = player.get_random_investors()
        
        # Initializing payoffs and investors lists so they are in order
        invest_payoff = []
        keep_payoff = []
        investors = []
        
        # Getting sample payoffs for each of the 20 draws
        for i in draws:
            investors.append(investors_rand[len(investors)])
            invest_payoff.append(C.investor_payoffs_sample['Low'][investors_rand[len(investors)-1] + 1])
            keep_payoff.append(i)

        # Creating a dictionary where draw numbers are keys and a list of corresponding values
        draw_dict = {
            i: {1: draws[i], 2: invest_payoff[i], 3: keep_payoff[i], 4: investors[i]}
            for i in range(20)
        }

        return {'draw_dict': draw_dict, 'invest_value': 250, 'quality': 'Low', 'advice': 'Invest', 'endowment': 300}
    

class P14(BaseReadyPage):
    pass


class QuizWaitPage(WaitPage):
    body_text = 'Waiting for all participants to complete the quiz'

    
class P15(BaseReadyPage):
    @staticmethod
    def js_vars(player):
        '''
        60 second timeout
        '''
        return dict(
            timeout_instr=60000,
        )
        
        
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing Stage 1 history to HTML and participant role
        '''
        role = 'Advisor' if player.participant.vars['role'] == 'Advisor' else 'Investor'
        return {'history': player.participant.vars['stage_1_history'], 'role': role}


class P16(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s1_advisor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs}


class P17(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s1_advisor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs}


class P18(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P11WaitPage, P12, P12WaitPage, P13, P14, QuizWaitPage, P15, P16, P17, P18]
