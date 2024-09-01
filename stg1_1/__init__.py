from otree.api import *
from settings import INSTRUCTIONS_TIME


doc = """
Stage 1 instructions app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg1_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout Seconds
    instructions_time = INSTRUCTIONS_TIME

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
    
    # Sample player history
    advisor_history = [
        {'round_number': 1, 'advisor_low_advice': 'Keep', 'advisor_med_advice': 'Keep', 'advisor_high_advice': 'Keep', 'group': {'estimated_signal': 'High', 'actual_signal': 'High', 'total_players_invest': 1, 'investor_payoff': '0 ECU'}, 'payoff': '3 ECU'},
        {'round_number': 2, 'advisor_low_advice': 'Keep', 'advisor_med_advice': 'Keep', 'advisor_high_advice': 'Invest', 'group': {'estimated_signal': 'Medium', 'actual_signal': 'Medium', 'total_players_invest': 3, 'investor_payoff': '6 ECU'}, 'payoff': '12 ECU'},
        {'round_number': 3, 'advisor_low_advice': 'Keep', 'advisor_med_advice': 'Invest', 'advisor_high_advice': 'Keep', 'group': {'estimated_signal': 'High', 'actual_signal': 'Low', 'total_players_invest': 4, 'investor_payoff': '1 ECU'}, 'payoff': '0 ECU'},
        {'round_number': 4, 'advisor_low_advice': 'Invest', 'advisor_med_advice': 'Invest', 'advisor_high_advice': 'Invest', 'group': {'estimated_signal': 'Low', 'actual_signal': 'High', 'total_players_invest': 4, 'investor_payoff': '24 ECU'}, 'payoff': '34 ECU'},
        {'round_number': 5, 'advisor_low_advice': 'Keep', 'advisor_med_advice': 'Keep', 'advisor_high_advice': 'Invest', 'group': {'estimated_signal': 'Low', 'actual_signal': 'Medium', 'total_players_invest': 2, 'investor_payoff': '0 ECU'}, 'payoff': '12 ECU'},
        {'round_number': 6, 'advisor_low_advice': 'Invest', 'advisor_med_advice': 'Invest', 'advisor_high_advice': 'Invest', 'group': {'estimated_signal': 'High', 'actual_signal': 'High', 'total_players_invest': 4, 'investor_payoff': '24 ECU'}, 'payoff': '34 ECU'},
    ]
    investor_history = [
        {'round_number': 1, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Invest', 'actual_signal': 'High', 'total_players_invest': 1, 'advisor_payoff': '3 ECU'}, 'other_investors': 0, 'payoff': '0 ECU'},
        {'round_number': 2, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Keep', 'actual_signal': 'Medium', 'total_players_invest': 3, 'advisor_payoff': '12 ECU'}, 'other_investors': 2, 'payoff': '6 ECU'},
        {'round_number': 3, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Invest', 'actual_signal': 'Low', 'total_players_invest': 4, 'advisor_payoff': '0 ECU'}, 'other_investors': 3, 'payoff': '1 ECU'},
        {'round_number': 4, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Invest', 'actual_signal': 'High', 'total_players_invest': 4, 'advisor_payoff': '34 ECU'}, 'other_investors': 3, 'payoff': '24 ECU'},
        {'round_number': 5, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Keep', 'actual_signal': 'Medium', 'total_players_invest': 2, 'advisor_payoff': '12 ECU'}, 'other_investors': 1, 'payoff': '0 ECU'},
        {'round_number': 6, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Invest', 'actual_signal': 'High', 'total_players_invest': 4, 'advisor_payoff': '34 ECU'}, 'other_investors': 3, 'payoff': '24 ECU'},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    # Not passed to data export
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    # ID field
    player_id = models.IntegerField(blank=False, label='', max=99)

    # Sample decision fields
    investor_decision = models.StringField(blank=False)
    advisor_low_advice = models.StringField(blank=False)
    advisor_med_advice = models.StringField(blank=False)
    advisor_high_advice = models.StringField(blank=False)


# PAGES
class BaseReadyPage(Page): # Creating base page
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        '''
        Making instruction pages conditional on all players in session clicking 'Continue'.
        See javascript for participant side
        '''
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}
    
    
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing the player payoff dictionaries and player role to HTML
        '''
        role = 'Advisor' if player.participant.vars['role'] == 'Advisor' else 'Investor'
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'role': role}


class P1(Page):
    form_model = 'player'
    form_fields = ['player_id']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        '''
        Storing ID to the participant and player field
        '''
        id = player.player_id
        player.participant.label = str(id)


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
    form_model = 'player'
    form_fields = ['advisor_low_advice', 'advisor_med_advice', 'advisor_high_advice']
    
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing player payoff dictionaries & sample Advisor history
        '''
        history = C.advisor_history
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(history)}


class P10WaitPage(WaitPage):
    body_text = 'Waiting until everyone has clicked continue'
    

class P11(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing player payoff dictionaries & sample Advisor history
        '''
        history = C.advisor_history
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(history)}


class P12(BaseReadyPage):
    form_model = 'player'
    form_fields = ['investor_decision']
    
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing player payoff dictionaries, sample Advisor's advice, & sample Investor history
        '''
        history = C.investor_history
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(history), 'advice': 'Invest'}


class P12WaitPage(WaitPage):
    body_text = 'Waiting until everyone has clicked continue'


class P13(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing player payoff dictionaries & sample Advisor history
        '''
        history = C.investor_history.copy()
        history.append(
            {'round_number': 7, 'investor_decision': 'Invest', 'group': {'advisor_advice': 'Invest', 'actual_signal': 'Medium', 'total_players_invest': 4, 'advisor_payoff': '12 ECU'}, 'other_investors': 3, 'payoff': '6 ECU'}
        )
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(history)}


class P14(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing player payoff dictionaries & sample Advisor history
        '''
        history = C.advisor_history.copy()
        history.append(
            {'round_number': 7, 'advisor_low_advice': 'Invest', 'advisor_med_advice': 'Keep', 'advisor_high_advice': 'Keep', 'group': {'estimated_signal': 'Low', 'actual_signal': 'Medium', 'total_players_invest': 4, 'investor_payoff': '6 ECU'}, 'payoff': '12 ECU'}
        )
        return {'advisor_table': C.stg1_advisor_payoffs, 'investor_table': C.stg1_investor_payoffs, 'history': reversed(history)}


class P15(BaseReadyPage):
    pass


class P16(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P10WaitPage, P11, P12, P12WaitPage, P13, P14, P15, P16]
