from otree.api import *
import random as r
from settings import GROUPING, DECISION_TIME, FEEDBACK_TIME

doc = """
Stage 2 scenario 1 app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_2'
    PLAYERS_PER_GROUP = GROUPING
    NUM_ROUNDS = 1

    # Timeout seconds for decision page
    decision_time = DECISION_TIME
    feedback_time = FEEDBACK_TIME

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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Group treatment field
    treatment = models.StringField()

    # Randomly drawn signal field
    actual_signal = models.StringField()
    
    # Advisor's advice
    advisor_advice = models.StringField()

    # Player functions meant to be passed to history participant field
    def advisor_payoff(self):
        '''
        Gets advisor payoff
        '''
        for p in self.get_players():
            if p.role == C.advisor_ROLE:
                return p.payoff


    def total_players_invest(self):
        '''
        Gets total investors who choose invest (i.e., their minimum endowment is greater than the random draw)
        '''
        return sum(1 for player in self.get_players() if player.role != C.advisor_ROLE and player.investor_minimum_endowment > player.random_draw)
    

class Player(BasePlayer):
    # Decision fields
    advisor_low_advice = models.StringField(blank=False)
    advisor_high_advice = models.StringField(blank=False)
    investor_minimum_endowment = models.IntegerField(blank=False, min=0, max=400)
    
    # Random draw field
    random_draw = models.IntegerField(min=0, max=400)

    # Player functions meant to be passed to history participant field
    def other_investors(self):
        '''
        Gets total other investors that invested
        '''
        if self.role != C.advisor_ROLE and self.investor_minimum_endowment > self.random_draw:
            return self.group.total_players_invest() - 1
        else:
            return self.group.total_players_invest()
    

    def investor_decision(self):
        '''
        Gets investor decision based on choosen minimum endowment and random draw
        '''
        if self.role != C.advisor_ROLE:
            if self.investor_minimum_endowment > self.random_draw:
                return 'Invest'
            else:
                return "Keep"


# Functions
def creating_session(subsession):
    '''
    Function the gets run before the start of the app.
    Sets group matrix and assigns treatments.
    '''
    # Retrieving group matrix from Stage 1
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])
    
    # Assigning treatments & randomly selecting signal
    groups = subsession.get_groups()
    treatments = ['LCLE', 'LCHE', 'HCLE', 'HCHE']
    for i, group in enumerate(groups):
        group.treatment = treatments[i % len(treatments)]
        
        # Assigning a Signal
        possible_signals = ['Low', 'High']
        group.actual_signal = r.choice(possible_signals)


def is_displayed_advisor(player: Player):
    '''
    Function to only display page if advisor
    '''
    return player.role == C.advisor_ROLE


def is_displayed_investor(player: Player):
    '''
    Function to only display page if investor
    '''
    return player.role != C.advisor_ROLE


# PAGES
class AdvisorDecision(Page):
    form_model = 'player'
    form_fields = ['advisor_low_advice', 'advisor_high_advice']
    is_displayed = is_displayed_advisor

    @staticmethod
    def js_vars(player):
        '''
        Passing timeout seconds defined in settings.py to Javascript
        '''
        return dict(
            timeout=C.decision_time,
        )


    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s1_advisor_payoffs, 'investor_table': C.stg2_s1_investor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs}


class InvestorDecision(Page):
    form_model = 'player'
    form_fields = ['investor_minimum_endowment']
    is_displayed = is_displayed_investor

    @staticmethod
    def js_vars(player):
        '''
        Passing timeout seconds defined in settings.py to Javascript
        '''
        return dict(
            timeout=C.decision_time,
        )


    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing the player payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s1_advisor_payoffs, 'investor_table': C.stg2_s1_investor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs}


class PayoffWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        '''
        Function to set payoffs once all players in group have made their decision(s)
        '''
        # Getting advisor's advice based on the signal
        if group.actual_signal == 'High':
            group.advisor_advice = group.get_player_by_role(C.advisor_ROLE).advisor_high_advice
        else:
            group.advisor_advice = group.get_player_by_role(C.advisor_ROLE).advisor_low_advice
        
        # Randomly selecting a draw for each 
        for player in group.get_players():
            if player.role != C.advisor_ROLE:
                player.random_draw = r.randint(1, 400)

        # Payoff dictionaries and signal
        investor_payoff = C.stg2_s1_investor_payoffs
        advisor_payoff = C.stg2_s1_advisor_payoffs
        signal = group.actual_signal

        # Defining payoffs
        for player in group.get_players():
            if player.group.advisor_advice == 'Invest':
                total_investors = group.total_players_invest()
            else:
                total_investors = 0
            
            if player.role != C.advisor_ROLE:
                if player.group.advisor_advice == 'Invest':
                    if player.investor_minimum_endowment > player.random_draw:
                        player.payoff = investor_payoff[signal][total_investors]
                    else:
                        player.payoff = player.random_draw
                else:
                    player.payoff = player.random_draw
            else:
                player.payoff = advisor_payoff[signal][total_investors]


class BeforeNextDecision(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        for player in subsession.get_players():
            signal = player.group.actual_signal
            if player.role != C.advisor_ROLE:
                player.participant.vars['scenario_1_history'] = {
                    'payoff': player.payoff, 
                    'signal': signal, 
                    'advice': player.group.advisor_advice, 
                    'draw': player.random_draw, 
                    'minimum_endowment': player.investor_minimum_endowment,
                    'other_investors': player.other_investors(),
                    }
            else:
                player.participant.vars['scenario_1_history'] = {
                    'payoff': player.payoff, 
                    'signal': signal, 
                    'advice': player.group.advisor_advice, 
                    }


page_sequence = [AdvisorDecision, InvestorDecision, PayoffWaitPage, BeforeNextDecision]