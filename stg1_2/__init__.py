from otree.api import *
from settings import GROUPING, DECISION_TIME, FEEDBACK_TIME, STAGE_1_ROUNDS

doc = """
Stage 1 app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg1_2'
    PLAYERS_PER_GROUP = GROUPING
    NUM_ROUNDS = STAGE_1_ROUNDS

    # Timeout seconds
    decision_time = DECISION_TIME
    feedback_time = FEEDBACK_TIME

    # Defining Role "Advisor"
    advisor_ROLE = 'Advisor'

    # Signal dictionaries
    treatment_signal = {
        'LCLE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 3, 16: 3, 17: 2, 18: 1, 19: 1, 20: 2, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'LCHE': {1: 3, 2: 1, 3: 3, 4: 3, 5: 3, 6: 3, 7: 2, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 1, 15: 3, 16: 3, 17: 2, 18: 1, 19: 1, 20: 2, 21: 3, 22: 2, 23: 1, 24: 2, 25: 3, 26: 2, 27: 1, 28: 1, 29: 3, 30: 1},
        'HCLE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 3, 16: 3, 17: 2, 18: 2, 19: 1, 20: 2, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
        'HCHE': {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 1, 15: 3, 16: 3, 17: 2, 18: 2, 19: 1, 20: 2, 21: 3, 22: 2, 23: 1, 24: 2, 25: 3, 26: 2, 27: 1, 28: 1, 29: 2, 30: 2},
    }
    actual_signals = {
        'LCLE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 1, 16: 3, 17: 2, 18: 1, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'LCHE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 1, 16: 3, 17: 2, 18: 1, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'HCLE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 1, 16: 3, 17: 2, 18: 2, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
        'HCHE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 1, 16: 3, 17: 2, 18: 2, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
    }

    # Signal decoder
    decoder = {1: 'Low', 2: 'Medium', 3: 'High', 'Low': 1, 'Medium': 2, 'High': 3}

    # Stage 1 payoff dictionaries & investor endowment
    investor_endowment = 12
    stg1_investor_payoffs = {
        'Low': {1: 0, 2: 0, 3: 1, 4: 1},
        'Medium': {1: 0, 2: 0, 3: 6, 4: 6},
        'High': {1: 0, 2: 0, 3: 24, 4: 24}
    }
    stg1_advisor_payoffs = {
        'Low': {0: 18, 1: 3, 2: 3, 3: 0, 4: 0},
        'Medium': {0: 5, 1: 5, 2: 12, 3: 12, 4: 12},
        'High': {0: 0, 1: 0, 2: 0, 3: 10, 4: 34}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Group treatment field
    treatment = models.StringField()

    # Fields to store signals (dependent on group treatment)
    estimated_signal = models.StringField()
    actual_signal = models.StringField()

    # Fields for continue validation & models to be passed on template
    advisor_advice = models.StringField()
    invest_count = models.IntegerField(initial=0)
    all_players_ready = models.IntegerField(initial=0)

    # Player functions meant to be passed to template in feedback/history tables
    def total_players_invest(self):
        '''
        Counts total investors who choose 'Invest'
        '''
        return sum(1 for player in self.get_players() if player.role != C.advisor_ROLE and player.investor_decision == 'Invest')


    def investor_payoff(self):
        '''
        Gets payoff for investor who choose 'Invest'
        '''
        for p in self.get_players():
            if p.role != C.advisor_ROLE and p.investor_decision == 'Invest':
                return p.payoff


    def advisor_payoff(self):
        '''
        Gets the group advisor's payoff
        '''
        for p in self.get_players():
            if p.role == C.advisor_ROLE:
                return p.payoff


class Player(BasePlayer):
    # Decision fields for advisor and investor
    investor_decision = models.StringField(blank=False)
    advisor_low_advice = models.StringField(blank=False)
    advisor_med_advice = models.StringField(blank=False)
    advisor_high_advice = models.StringField(blank=False)

    # Player functions meant to be passed to template in feedback/history tables
    def investors_decision(self):
        '''
        Gets investor's decision for history table
        '''
        if self.role != C.advisor_ROLE:
            if self.payoff == C.investor_endowment:
                return "Keep"
            else:
                return "Invest"


    def other_investors(self):
        '''
        Gets the amount of other investors who choose invest for an investor minus 1 if the player choose 'Invest'
        '''
        if self.investors_decision() == 'Invest':
            others = (self.group.total_players_invest() - 1)
            return others
        else:
            return self.group.total_players_invest()


# Functions
def creating_session(subsession):
    '''
    Function the gets run before the start of the app.
    Sets group matrix and assigns treatments.
    '''
    # Setting Group Matrix
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])

    # Assigning Treatments
    groups = subsession.get_groups()
    treatments = ['HCHE', 'HCLE', 'LCLE', 'LCHE']
    for i, group in enumerate(groups):
        group.treatment = treatments[i % len(treatments)]


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


def get_estimated_signal(round_number, treatment):
    '''
    Function to get estimated signal based on round number and treatment
    '''
    treatment_signal = C.treatment_signal
    decoder = C.decoder
    estimated_signal = decoder[treatment_signal[treatment][round_number]]
    return estimated_signal


# PAGES
class AdvisorDecision(Page):
    form_model = 'player'
    form_fields = ['advisor_low_advice', 'advisor_med_advice', 'advisor_high_advice']
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
        Passing the player payoff dictionaries and player history to HTML
        '''
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(player.in_previous_rounds())}


class InvestorWaitPage(WaitPage):
    body_text = 'Waiting for Advisor to give investment advice'
    is_displayed = is_displayed_investor


class InvestorDecision(Page):
    form_model = 'player'
    form_fields = ['investor_decision']
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
        Passing the player payoff dictionaries, advisor's advice, and player history to HTML
        '''
        # Getting the Advisor's advice based on the estimated signal
        estimated_signal = get_estimated_signal(player.round_number, player.group.treatment)
        advice_dict = {
            'Low': player.group.get_player_by_role(C.advisor_ROLE).advisor_low_advice, 
            'Medium': player.group.get_player_by_role(C.advisor_ROLE).advisor_med_advice, 
            'High': player.group.get_player_by_role(C.advisor_ROLE).advisor_high_advice}
        advice = advice_dict[estimated_signal]
        
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'advice': advice, 'history': reversed(player.in_previous_rounds())}


class BetweenWaitPage(Page):
    @staticmethod
    def live_method(player: Player, data):
        '''
        Conditional waitpage submission once all players in a group have made decisions
        '''
        player.group.all_players_ready += 1
        players = len(player.group.get_players())
        if player.group.all_players_ready == players:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing: player payoff dictionaries, estimated signal, advisor's/investor's decisions, advisor's advice, and player history to HTML
        '''
        if player.role == C.advisor_ROLE:
            estimated_signal = get_estimated_signal(player.round_number, player.group.treatment)
            
            # Advisor decisions
            low = player.advisor_low_advice
            med = player.advisor_med_advice
            high = player.advisor_high_advice
            
            return {'estimated_signal': estimated_signal, 'low': low, 'med': med, 'high': high, 'history': reversed(player.in_previous_rounds()), 'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs}
        else:
            # Getting the Advisor's advice based on the estimated signal
            estimated_signal = get_estimated_signal(player.round_number, player.group.treatment)
            advice_dict = {
                'Low': player.group.get_player_by_role(C.advisor_ROLE).advisor_low_advice,
                'Medium': player.group.get_player_by_role(C.advisor_ROLE).advisor_med_advice,
                'High': player.group.get_player_by_role(C.advisor_ROLE).advisor_high_advice}
            advice = advice_dict[estimated_signal]
            
            # Investor decision
            decision = player.investor_decision
            
            return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'advice': advice, 'decision': decision, 'history': reversed(player.in_previous_rounds())}


class PayoffWaitPage(WaitPage):
    # Defining Payoffs
    @staticmethod
    def after_all_players_arrive(group: Group):
        '''
        Function to set payoffs once all players in group have made their decision(s)
        '''
        # Player payoff dictionaries
        investor_payoff = C.stg1_investor_payoffs
        advisor_payoff = C.stg1_advisor_payoffs
        
        # Getting the appropriate signals based on round number and treatment
        round_number = group.round_number
        treatment = group.treatment
        decoder = C.decoder
        treatment_signal = C.treatment_signal
        actual_signals = C.actual_signals
        group.estimated_signal = decoder[treatment_signal[treatment][round_number]]
        group.actual_signal = decoder[actual_signals[treatment][round_number]]
        
        # Getting the Advisor's advice based on the estimated signal
        estimated_signal = group.estimated_signal
        actual_signal = group.actual_signal
        advice_dict = {
            'Low': group.get_player_by_role(C.advisor_ROLE).advisor_low_advice, 'Medium': group.get_player_by_role(C.advisor_ROLE).advisor_med_advice, 'High': group.get_player_by_role(C.advisor_ROLE).advisor_high_advice}
        group.advisor_advice = advice_dict[estimated_signal]

        # Counting investors based on Advisor's advice & payoffs
        group.invest_count = sum(1 for player in group.get_players() if player.role != C.advisor_ROLE and player.investor_decision == 'Invest')
        
        # Setting player payoffs
        for player in group.get_players():
            if player.role == C.advisor_ROLE:
                player.payoff = advisor_payoff[actual_signal][group.invest_count]
            else:
                if player.investor_decision == 'Invest':
                    player.payoff = investor_payoff[actual_signal][group.invest_count]
                else:
                    player.payoff = C.investor_endowment


class Feedback(Page):
    timeout_seconds = C.feedback_time

    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing the player payoff dictionaries, advisor's advice, and player history to HTML
        '''
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(player.in_all_rounds())}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        '''
        Storing Stage 1 player history and payoff to particiant vars.
        Used to call back for final payoff screen at end of experiment.
        '''
        # Player Stage 1 payoff
        player.participant.vars['stage_1_payoff'] += player.payoff
        
        # Player history based on player role
        if player.role == C.advisor_ROLE:
            history_data = [
                {
                    'round_number': p.round_number, 
                    'advisor_low_advice': p.advisor_low_advice, 
                    'advisor_med_advice': p.advisor_med_advice, 
                    'advisor_high_advice': p.advisor_high_advice, 
                    'estimated_signal': p.group.estimated_signal, 
                    'actual_signal': p.group.actual_signal, 
                    'total_players_invest': p.group.total_players_invest(), 
                    'payoff': p.payoff, 
                    'investor_payoff': p.group.investor_payoff()
                    }
                for p in player.in_all_rounds()
            ]
        else:
            history_data = [
                {
                    'round_number': p.round_number, 
                    'advisor_advice': p.group.advisor_advice, 
                    'investor_decision': p.investor_decision, 
                    'other_investors': p.other_investors(), 
                    'total_players_invest': p.group.total_players_invest(), 
                    'actual_signal': p.group.actual_signal, 
                    'payoff': p.payoff, 
                    'advisor_payoff': p.group.advisor_payoff()
                    }
                for p in player.in_all_rounds()
            ]
        player.participant.vars['stage_1_history'] = history_data


class BeforeNextRound(WaitPage):
    wait_for_all_groups = True
    title_text = 'Next Round Will Start Soon'
    body_text = 'Waiting for other participants'

    @staticmethod
    def is_displayed(player: Player):
        '''
        Only shown if round number < 30 (or total number of rounds)
        '''
        return player.round_number != C.NUM_ROUNDS


class BeforeNextStage(WaitPage):
    wait_for_all_groups = True
    title_text = 'End of Stage 1'
    body_text = 'Instructions for Stage 2 will begin when all players are ready'

    @staticmethod
    def is_displayed(player: Player):
        '''
        Only shown if round number = 30 (or total number of rounds)
        '''
        return player.round_number == C.NUM_ROUNDS


page_sequence = [AdvisorDecision, InvestorWaitPage, InvestorDecision, BetweenWaitPage, PayoffWaitPage, Feedback, BeforeNextRound, BeforeNextStage]