from otree.api import *
from settings import grouping, DECISION_TIME, FEEDBACK_TIME

doc = """
Stage stg1_2 Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg1_2'
    PLAYERS_PER_GROUP = grouping
    NUM_ROUNDS = 5

    # Timeout seconds
    decision_time = DECISION_TIME
    feedback_time = FEEDBACK_TIME

    # Defining Role "Advisor"
    pa_ROLE = 'Advisor'

    # Signal Dictionaries
    treatment_signal = {
        'LCLE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 3, 16: 3,
                 17: 2, 18: 1, 19: 1, 20: 2, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'LCHE': {1: 3, 2: 1, 3: 3, 4: 3, 5: 3, 6: 3, 7: 2, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 1, 15: 3, 16: 3,
                 17: 2, 18: 1, 19: 1, 20: 2, 21: 3, 22: 2, 23: 1, 24: 2, 25: 3, 26: 2, 27: 1, 28: 1, 29: 3, 30: 1},
        'HCLE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 3, 16: 3,
                 17: 2, 18: 2, 19: 1, 20: 2, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
        'HCHE': {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 1, 15: 3, 16: 3,
                 17: 2, 18: 2, 19: 1, 20: 2, 21: 3, 22: 2, 23: 1, 24: 2, 25: 3, 26: 2, 27: 1, 28: 1, 29: 2, 30: 2},
    }
    actual_signals = {
        'LCLE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 1, 16: 3,
                 17: 2, 18: 1, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'LCHE': {1: 3, 2: 1, 3: 1, 4: 3, 5: 1, 6: 3, 7: 3, 8: 2, 9: 3, 10: 1, 11: 3, 12: 2, 13: 1, 14: 3, 15: 1, 16: 3,
                 17: 2, 18: 1, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 3, 30: 1},
        'HCLE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 1, 16: 3,
                 17: 2, 18: 2, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
        'HCHE': {1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 3, 7: 2, 8: 2, 9: 2, 10: 1, 11: 3, 12: 2, 13: 2, 14: 3, 15: 1, 16: 3,
                 17: 2, 18: 2, 19: 1, 20: 3, 21: 2, 22: 2, 23: 1, 24: 2, 25: 3, 26: 3, 27: 1, 28: 1, 29: 2, 30: 2},
    }

    # Signal decoder
    decoder = {1: 'Low', 2: 'Medium', 3: 'High', 'Low': 1, 'Medium': 2, 'High': 3}

    # Stage 1 Payoff dictionaries & Investor endowment
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 1, 4: 1},
        2: {1: 0, 2: 0, 3: 6, 4: 6},
        3: {1: 0, 2: 0, 3: 24, 4: 24}
    }
    pa_payoff = {
        1: {0: 18, 1: 3, 2: 3, 3: 0, 4: 0},
        2: {0: 5, 1: 5, 2: 12, 3: 12, 4: 12},
        3: {0: 0, 1: 0, 2: 0, 3: 10, 4: 34}
    }
    pb_endowment = 12


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Group treatment field
    treatment = models.StringField()

    # Fields to store signals (dependent on group treatment)
    estimated_signal = models.StringField()
    actual_signal = models.StringField()

    # Fields for continue validation & models to be passed on template
    pa_advice = models.StringField()
    invest_count = models.IntegerField(initial=0)
    all_players_ready = models.IntegerField(initial=0)

    # Player history functions meant to be passed to template in feedback page
    def total_players_invest(self):
        return sum(1 for player in self.get_players() if player.role != C.pa_ROLE and player.pb_decision == 'Invest')

    def pb_payoff(self):
        for p in self.get_players():
            if p.role != C.pa_ROLE and p.pb_decision == 'Invest':
                return p.payoff

    def pa_payoff(self):
        for p in self.get_players():
            if p.role == C.pa_ROLE:
                return p.payoff


class Player(BasePlayer):
    # Decision fields for Advisor and Investor
    pb_decision = models.StringField(blank=False)
    pa_low_advice = models.StringField(blank=False)
    pa_med_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)

    # Player history functions meant to be passed to template in feedback page
    def player_decision(self):
        if self.role != C.pa_ROLE:
            if self.payoff == C.pb_endowment:
                return "Keep"
            else:
                return "Invest"

    def other_investors(self):
        if self.player_decision() == 'Invest':
            others = (self.group.total_players_invest() - 1)
            return others
        else:
            return self.group.total_players_invest()


# Functions
def creating_session(subsession):
    # Setting Group Matrix
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])

    # Assigning Treatments
    groups = subsession.get_groups()
    treatments = ['LCLE', 'LCHE', 'HCLE', 'HCHE']
    for i, group in enumerate(groups):
        group.treatment = treatments[i % len(treatments)]


def is_displayed_pa(player: Player):
    # Is displayed function for role Investor
    return player.role == C.pa_ROLE


def is_displayed_pb(player: Player):
    # Is displayed function for role Advisor
    return player.role != C.pa_ROLE


# PAGES
class P1_PADecision(Page):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_med_advice', 'pa_high_advice']
    is_displayed = is_displayed_pa

    @staticmethod
    def js_vars(player):
        return dict(
            timeout=C.decision_time,
        )

    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff, 'history': reversed(player.in_previous_rounds())}


class PlayerBWaitPage(WaitPage):
    body_text = 'Waiting for Advisor to give investment advice'
    is_displayed = is_displayed_pb


class P1_PBDecision(Page):
    form_model = 'player'
    form_fields = ['pb_decision']
    is_displayed = is_displayed_pb

    @staticmethod
    def js_vars(player):
        return dict(
            timeout=C.decision_time,
        )

    @staticmethod
    def vars_for_template(player: Player):
        # Returning the Advisors advice to the Investors
        treatment_signal = C.treatment_signal
        round_number = player.round_number
        treatment = player.group.treatment
        decoder = C.decoder
        estimated_signal = decoder[treatment_signal[treatment][round_number]]
        advice_dict = {'Low': player.group.get_player_by_role(C.pa_ROLE).pa_low_advice, 'Medium': player.group.get_player_by_role(C.pa_ROLE).pa_med_advice, 'High': player.group.get_player_by_role(C.pa_ROLE).pa_high_advice}
        advice = advice_dict[estimated_signal]
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff, 'advice': advice, 'history': reversed(player.in_previous_rounds())}


class P2_BetweenWaitPage(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players = len(player.group.get_players())
        if player.group.all_players_ready == players:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        if player.role == C.pa_ROLE:
            treatment_signal = C.treatment_signal
            round_number = player.round_number
            treatment = player.group.treatment
            decoder = C.decoder
            estimated_signal = decoder[treatment_signal[treatment][round_number]]
            low = player.pa_low_advice
            med = player.pa_med_advice
            high = player.pa_high_advice
            return {'estimated_signal': estimated_signal, 'low': low, 'med': med, 'high': high, 'history': reversed(player.in_previous_rounds()), 'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}
        else:
            treatment_signal = C.treatment_signal
            round_number = player.round_number
            treatment = player.group.treatment
            decoder = C.decoder
            estimated_signal = decoder[treatment_signal[treatment][round_number]]
            advice_dict = {'Low': player.group.get_player_by_role(C.pa_ROLE).pa_low_advice,
                           'Medium': player.group.get_player_by_role(C.pa_ROLE).pa_med_advice,
                           'High': player.group.get_player_by_role(C.pa_ROLE).pa_high_advice}
            advice = advice_dict[estimated_signal]
            decision = player.pb_decision
            return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff, 'advice': advice, 'decision': decision, 'history': reversed(player.in_previous_rounds())}


class PayoffWaitPage(WaitPage):
    # Defining Payoffs
    @staticmethod
    def after_all_players_arrive(group: Group):
        pb_payoff = C.pb_payoff
        pa_payoff = C.pa_payoff
        round_number = group.round_number
        treatment = group.treatment
        decoder = C.decoder
        treatment_signal = C.treatment_signal
        actual_signals = C.actual_signals
        group.estimated_signal = decoder[treatment_signal[treatment][round_number]]
        group.actual_signal = decoder[actual_signals[treatment][round_number]]
        estimated_signal = group.estimated_signal
        actual_signal = group.actual_signal
        advice_dict = {'Low': group.get_player_by_role(C.pa_ROLE).pa_low_advice, 'Medium': group.get_player_by_role(C.pa_ROLE).pa_med_advice, 'High': group.get_player_by_role(C.pa_ROLE).pa_high_advice}
        group.pa_advice = advice_dict[estimated_signal]

        # Counting investors based on Advisors advice & Payoffs
        group.invest_count = sum(1 for player in group.get_players() if player.role != C.pa_ROLE and player.pb_decision == 'Invest')
        for player in group.get_players():
            if player.role == C.pa_ROLE:
                player.payoff = pa_payoff[decoder[actual_signal]][group.invest_count]
            else:
                if player.pb_decision == 'Invest':
                    player.payoff = pb_payoff[decoder[actual_signal]][group.invest_count]
                else:
                    player.payoff = C.pb_endowment


class P3_Feedback(Page):
    timeout_seconds = C.feedback_time

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff, 'history': reversed(player.in_all_rounds())}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['STG1_payoff'] += player.payoff
        if player.role == C.pa_ROLE:
            history_data = [
                {'round_number': p.round_number, 'pa_low_advice': p.pa_low_advice, 'pa_med_advice': p.pa_med_advice,
                 'pa_high_advice': p.pa_high_advice, 'estimated_signal': p.group.estimated_signal, 'actual_signal': p.group.actual_signal,
                 'total_players_invest': p.group.total_players_invest(), 'payoff': p.payoff, 'pb_payoff': p.group.pb_payoff()}
                for p in player.in_all_rounds()
            ]
            # Store the formatted history in advisor participant vars
            player.participant.vars['STG1_history'] = history_data
        else:
            history_data = [
                {'round_number': p.round_number, 'pa_advice': p.group.pa_advice, 'pb_decision': p.pb_decision,
                 'other_investors': p.other_investors(), 'total_players_invest': p.group.total_players_invest(),
                 'actual_signal': p.group.actual_signal, 'payoff': p.payoff, 'pa_payoff': p.group.pa_payoff()}
                for p in player.in_all_rounds()
            ]
            # Store the formatted history in investor participant vars
            player.participant.vars['STG1_history'] = history_data


class BeforeNextRound(WaitPage):
    wait_for_all_groups = True
    title_text = 'Next Round Will Start Soon'
    body_text = 'Waiting for other participants'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number != C.NUM_ROUNDS


class BeforeNextStage(WaitPage):
    wait_for_all_groups = True
    title_text = 'End of Stage 1'
    body_text = 'Instructions for Stage 2 will begin when all players are ready'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [P1_PADecision, PlayerBWaitPage, P1_PBDecision, P2_BetweenWaitPage, PayoffWaitPage, P3_Feedback, BeforeNextRound, BeforeNextStage]