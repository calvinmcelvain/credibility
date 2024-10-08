from otree.api import *
import random as r
from settings import GROUPING, DECISION_TIME, FEEDBACK_TIME

doc = """
Stage 2 scenario 3 app
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_6'
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
    # Group treatment field
    treatment = models.StringField()
    
    # Advisor's advice
    advisor_advice = models.StringField()

    # Randomly drawn fields
    decision_towards_payment = models.IntegerField()
    actual_signal = models.StringField()
    
    # Previous total investors
    s1_total_investors = models.IntegerField(initial=0)
    s2_total_investors = models.IntegerField(initial=0)
    s3_total_investors = models.IntegerField(initial=0)

    # Player functions meant to be passed to history participant field
    def investor_payoff(self):
        for p in self.get_players():
            if p.role != C.pa_ROLE and p.pb_outside_option > p.random_draw:
                return p.payoff
            
    
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
    
    # Random draw
    random_draw = models.IntegerField(min=0, max=400)
    
    # Final decision fields
    final_s1_minimum_endowment = models.IntegerField(blank=False, min=0, max=400)
    final_s2_minimum_endowment = models.IntegerField(blank=False, min=0, max=400)
    final_s3_minimum_endowment = models.IntegerField(blank=False, min=0, max=400)
    
    # Final payoff fields
    final_s1_payoff = models.CurrencyField()
    final_s2_payoff = models.CurrencyField()
    final_s3_payoff = models.CurrencyField()
    
    # Demographics fields
    gender = models.StringField(blank=False)
    age = models.IntegerField(blank=False)
    ethnicity = models.StringField(blank=False)
    hol = models.StringField(blank=False)

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
    
    # Randomly choosing decision to count
    for group in subsession.get_groups():
        group.decision_towards_payment = r.randint(1, 3)


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
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 'investor_table': C.stg2_s3_investor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


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
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 'investor_table': C.stg2_s3_investor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


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
                player.random_draw = r.randint(0, 400)

        # Payoff dictionaries and signal
        investor_payoff = C.stg2_s3_investor_payoffs
        advisor_payoff = C.stg2_s3_advisor_payoffs
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


class FinalConfirmation(Page):
    form_model = 'player'
    form_fields = ['final_s1_minimum_endowment', 'final_s2_minimum_endowment', 'final_s3_minimum_endowment']
    is_displayed = is_displayed_investor
    
    @staticmethod
    def js_vars(player):
        '''
        Passing previous endowments to Javascript
        '''
        s1_decision = player.participant.vars['scenario_1_history']['minimum_endowment']
        s2_decision = player.participant.vars['scenario_2_history']['minimum_endowment']
        s3_decision = player.investor_minimum_endowment
        return {'s1': s1_decision, 's2': s2_decision, 's3': s3_decision}
    
    
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing all investor payoff dictionaries to HTML
        '''
        return {'advisor_table': C.stg2_s3_advisor_payoffs, 's1_investor_table': C.stg2_s1_investor_payoffs, 's2_investor_table': C.stg2_s2_investor_payoffs, 's3_investor_table': C.stg2_s3_investor_payoffs}


class FinalPayoffWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for i in group.get_players():
            # Advice
            s1_advice = i.participant.vars['scenario_1_history']['advice']
            s2_advice = i.participant.vars['scenario_2_history']['advice']
            s3_advice = group.advisor_advice
            
            # Signals
            s1_signal = i.participant.vars['scenario_1_history']['signal']
            s2_signal = i.participant.vars['scenario_2_history']['signal']
            s3_signal = group.actual_signal

        # Total investors
        s1_total_investors = sum(1 for player in group.get_players() if player.role != C.advisor_ROLE and player.final_s1_minimum_endowment > player.participant.vars['scenario_1_history']['draw'] and s1_advice == 'Invest')
        s2_total_investors = sum(1 for player in group.get_players() if player.role != C.advisor_ROLE and player.final_s2_minimum_endowment > player.participant.vars['scenario_2_history']['draw'] and s2_advice == 'Invest')
        s3_total_investors = sum(1 for player in group.get_players() if player.role != C.advisor_ROLE and player.final_s3_minimum_endowment > player.random_draw and s3_advice == 'Invest')
        
        # Payoff Dictionaries
        s1_investor_payoff = C.stg2_s1_investor_payoffs
        s2_investor_payoff = C.stg2_s2_investor_payoffs
        s3_investor_payoff = C.stg2_s3_investor_payoffs
        advisor_payoff = C.stg2_s3_advisor_payoffs

        # Defining payoffs
        for player in group.get_players():
            if player.role != C.advisor_ROLE:
                # Scenario 1 payoffs
                s1_random_draw = player.participant.vars['scenario_1_history']['draw']
                player.group.s1_total_investors = s1_total_investors
                if player.final_s1_minimum_endowment > s1_random_draw and s1_advice == 'Invest':
                    player.final_s1_payoff = s1_investor_payoff[s1_signal][s1_total_investors]
                else:
                    player.final_s1_payoff = s1_random_draw
                
                # Scenario 2 payoffs
                s2_random_draw = player.participant.vars['scenario_2_history']['draw']
                player.group.s2_total_investors = s2_total_investors
                if player.final_s2_minimum_endowment > s2_random_draw and s2_advice == 'Invest':
                    player.final_s2_payoff = s2_investor_payoff[s2_signal][s2_total_investors]
                else:
                    player.final_s2_payoff = s2_random_draw

                # Scenario 3 payoffs
                s3_random_draw = player.random_draw
                player.group.s3_total_investors = s3_total_investors
                if player.final_s3_minimum_endowment > s3_random_draw and s3_advice == 'Invest':
                    player.final_s3_payoff = s3_investor_payoff[s3_signal][s3_total_investors]
                else:
                    player.final_s3_payoff = s3_random_draw
            else:
                # Scenario 1 payoffs
                player.final_s1_payoff = advisor_payoff[s1_signal][s1_total_investors]           
                
                # Scenario 2 payoffs
                player.final_s2_payoff = advisor_payoff[s2_signal][s2_total_investors]
                
                # Scenario 3 payoffs
                player.final_s3_payoff = advisor_payoff[s3_signal][s3_total_investors]


class GatherGroupsWaitPage(WaitPage):
    wait_for_all_groups = True
    doc = '''
    The reason for back-to-back waitpages is due to calling the method 'after_all_players_arrive' after setting 'wait_for_all_groups' to True. Then the method must be a Subsession function. Easier to define this waitpage then re-code previous waitpage.
    '''        


class FinalScreen(Page):
    @staticmethod
    def vars_for_template(player: Player):
        '''
        Passing all scenario history data and calculating final payoffs
        '''
        # Stage 1
        stage_1_payoff = player.participant.vars['stage_1_payoff']
        real_stage_1_payoff = stage_1_payoff.to_real_world_currency(player.session)
        
        # Stage 2
        counted_decision = player.group.decision_towards_payment
        scenario_payoffs = {
            1: player.final_s1_payoff,
            2: player.final_s2_payoff,
            3: player.final_s3_payoff,
        }
        stage_2_payoff = scenario_payoffs[counted_decision]
        real_stage_2_payoff = stage_2_payoff.to_real_world_currency(player.session)
        
        # Calculating final payoffs
        fee = player.session.config['participation_fee']
        final_payoff = stage_1_payoff + stage_2_payoff
        real_final_payoff = final_payoff.to_real_world_currency(player.session)
        player.participant.payoff = final_payoff
        final = player.participant.payoff_plus_participation_fee()
        
        # Getting scenario history
        s1_advice = player.participant.vars['scenario_1_history']['advice']
        s2_advice = player.participant.vars['scenario_2_history']['advice']
        s3_advice = player.group.advisor_advice
        history = {
                1: {'signal': player.participant.vars['scenario_1_history']['signal'], 
                    'advice': s1_advice,
                    'investors': player.group.s1_total_investors,
                    'payoff': player.final_s1_payoff},
                2: {'signal': player.participant.vars['scenario_2_history']['signal'], 
                    'advice': s2_advice,
                    'investors': player.group.s2_total_investors,
                    'payoff': player.final_s2_payoff},
                3: {'signal': player.group.actual_signal, 
                    'advice': s3_advice,
                    'investors': player.group.s3_total_investors,
                    'payoff': player.final_s3_payoff},
            }
        if player.role != C.advisor_ROLE:
            history[1]['draw'] = player.participant.vars['scenario_1_history']['draw']
            history[1]['decision'] = 'Invest' if s1_advice == 'Invest' and player.final_s1_minimum_endowment > player.participant.vars['scenario_1_history']['draw'] else 'Keep'
            history[1]['other_investors'] = player.group.s1_total_investors - 1 if history[1]['decision'] == 'Invest' else player.group.s1_total_investors
            history[1]['advisor_payoff'] = player.group.get_player_by_role(C.advisor_ROLE).final_s1_payoff
            history[2]['draw'] = player.participant.vars['scenario_2_history']['draw']
            history[2]['decision'] = 'Invest' if s2_advice == 'Invest' and player.final_s2_minimum_endowment > player.participant.vars['scenario_2_history']['draw'] else 'Keep'
            history[2]['other_investors'] = player.group.s2_total_investors - 1 if history[2]['decision'] == 'Invest' else player.group.s2_total_investors
            history[2]['advisor_payoff'] = player.group.get_player_by_role(C.advisor_ROLE).final_s2_payoff
            history[3]['draw'] = player.random_draw
            history[3]['decision'] = 'Invest' if s3_advice == 'Invest' and player.final_s3_minimum_endowment > player.random_draw else 'Keep'
            history[3]['other_investors'] = player.group.s3_total_investors - 1 if history[3]['decision'] == 'Invest' else player.group.s3_total_investors
            history[3]['advisor_payoff'] = player.group.get_player_by_role(C.advisor_ROLE).final_s3_payoff
            

        return {'final_payoff': final_payoff, 
                'Stage_1': stage_1_payoff, 
                'Stage_2': stage_2_payoff,
                'real_final': real_final_payoff, 
                'real_Stage_1': real_stage_1_payoff, 
                'real_Stage_2': real_stage_2_payoff,
                'final': final, 
                'decision_counts': counted_decision, 
                'history': history, 
                'fee': fee}


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'ethnicity', 'hol']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.finished = True


class End(Page):
    pass


page_sequence = [AdvisorDecision, InvestorDecision, PayoffWaitPage, GatherGroupsWaitPage, FinalConfirmation, FinalPayoffWaitPage, GatherGroupsWaitPage, FinalScreen, Demographics, End]