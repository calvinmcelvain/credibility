from otree.api import *
import random


doc = """
Stage 2 Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG2_GAME'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3

    # Timeout seconds for decision page
    decision_time = 600
    feedback_time = 300

    # Defining "Player A" role
    pa_ROLE = 'Player A'

    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

    # Decision Payoff dictionaries
    pb_payoffs = {
        1: {1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, 3: {1: 300, 2: 300, 3: 300, 4: 300, 5: 300}},
        2: {1: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300}, 3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300}},
        3: {1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, 3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300}}
    }
    pa_payoffs = {
        1: {1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}, 3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}},
        2: {1: {0: 0, 1: 0, 2: 0, 3: 300, 4: 300, 5: 300}, 3: {0: 0, 1: 0, 2: 0, 3: 300, 4: 300, 5: 300}},
        3: {1: {0: 0, 1: 0, 2: 0, 3: 300, 4: 300, 5: 300}, 3: {0: 0, 1: 0, 2: 0, 3: 300, 4: 300, 5: 300}}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Group treatment field
    treatment = models.StringField()

    # Randomly drawn fields
    actual_signal = models.StringField()
    decision_towards_payment = models.IntegerField()

    # Chosen stage 2 payoff
    def chosen_payoff(self):
        for player in self.get_players():
            payoff = player.in_round(self.in_round(1).decision_towards_payment).payoff
            return payoff

    # Player history functions meant to be passed to template in feedback page
    def pb_payoff(self):
        for p in self.get_players():
            if p.role != C.pa_ROLE and p.pb_outside_option <= p.random_draw:
                return p.payoff
            elif p.role != C.pa_ROLE and p.pb_outside_option > p.random_draw:
                return p.payoff

    def pa_payoff(self):
        for p in self.get_players():
            if p.role == C.pa_ROLE:
                return p.payoff

    def total_players_invest(self):
        return sum(1 for player in self.get_players() if player.role != C.pa_ROLE and player.pb_outside_option <= player.random_draw)


class Player(BasePlayer):
    # Decision fields for Player A and B
    pa_low_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)
    pb_outside_option = models.IntegerField(blank=False, min=0, max=300)
    random_draw = models.IntegerField(min=0, max=300)

    # Player history functions meant to be passed to template in feedback page
    def other_investors(self):
        if self.role != C.pa_ROLE and self.pb_outside_option <= self.group.random_draw:
            others = (self.group.total_players_invest() - 1)
            return others
        else:
            return self.group.total_players_invest()


# Functions
def creating_session(subsession):
    # Retrieving group matrix from Stage 1
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])

    # Randomly choosing decision to count
    for group in subsession.get_groups():
        group.decision_towards_payment = random.randint(1, 3)


def is_displayed_pa(player: Player):
    # Is displayed function for role Player A
    return player.role == C.pa_ROLE

def is_displayed_pb(player: Player):
    # Is displayed function for role Player B
    return player.role != C.pa_ROLE


# PAGES
class P1_PADecision(Page):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_high_advice']
    timeout_seconds = C.decision_time
    is_displayed = is_displayed_pa

    @staticmethod
    def vars_for_template(player: Player):
        possible_signals = ['Low', 'High']
        player.group.actual_signal = random.choice(possible_signals)
        signal = player.group.actual_signal
        pb_payoff_table = C.pb_payoffs[player.round_number]
        pa_payoff_table = C.pa_payoffs[player.round_number]
        pa_table_preprocessed = {key: list(value.values()) for key, value in pa_payoff_table.items()}
        pb_table_preprocessed = {key: list(value.values()) for key, value in pb_payoff_table.items()}
        return {'signal': signal, 'pa_table': pa_table_preprocessed, 'pb_table': pb_table_preprocessed}


class PlayerBWaitPage(WaitPage):
    body_text = 'Waiting for Player A to give investment advice'
    is_displayed = is_displayed_pb

    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            if player.role != C.pa_ROLE:
                player.random_draw = random.randint(1, 300)


class P1_PBDecision(Page):
    form_model = 'player'
    form_fields = ['pb_outside_option']
    is_displayed = is_displayed_pb
    timeout_seconds = C.decision_time

    @staticmethod
    def vars_for_template(player: Player):
        if player.group.actual_signal == 'High':
            advice = player.group.get_player_by_role(C.pa_ROLE).pa_high_advice
        else:
            advice = player.group.get_player_by_role(C.pa_ROLE).pa_low_advice

        pb_payoff_table = C.pb_payoffs[player.round_number]
        pa_payoff_table = C.pa_payoffs[player.round_number]
        pa_table_preprocessed = {key: list(value.values()) for key, value in pa_payoff_table.items()}
        pb_table_preprocessed = {key: list(value.values()) for key, value in pb_payoff_table.items()}
        return {'advice': advice, 'pa_table': pa_table_preprocessed, 'pb_table': pb_table_preprocessed}


class PayoffWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        # Payoff Dictionaries
        pb_payoff = C.pb_payoffs
        pa_payoff = C.pa_payoffs
        signal = group.actual_signal

        # Defining payoffs
        decoder = C.decoder
        for player in group.get_players():
            if player.role != C.pa_ROLE:
                if player.pb_outside_option <= player.random_draw:
                    player.payoff = pb_payoff[player.round_number][decoder[signal]][group.total_players_invest()]
                else:
                    player.payoff = player.random_draw
            else:
                player.payoff = pa_payoff[player.round_number][decoder[signal]][group.total_players_invest()]


class P2_FinalScreen(Page):
    timeout_seconds = C.feedback_time

    @staticmethod
    def vars_for_template(player: Player):
        stage1_payoff = player.participant.vars['Stage1_payoff']
        stage2_payoff = player.group.chosen_payoff()

        # Calculating Participant payoff (Based on chosen decision)
        remainder = (player.participant.payoff - stage1_payoff - player.in_round(player.group.in_round(1).decision_towards_payment).payoff)
        player.participant.payoff = (player.participant.payoff - remainder)

        final_payoff = player.participant.payoff
        real_stg1 = stage2_payoff.to_real_world_currency(player.session)
        real_stg2 = stage1_payoff.to_real_world_currency(player.session)
        real_final = final_payoff.to_real_world_currency(player.session)
        final = player.participant.payoff_plus_participation_fee()
        decision_counts = player.group.in_round(1).decision_towards_payment
        return {'final_payoff': final_payoff, 'Stage_1': stage1_payoff, 'Stage_2': stage2_payoff
                , 'real_final': real_final, 'real_Stage_1': real_stg1, 'real_Stage_2': real_stg2,
                'final': final, 'decision_counts': decision_counts, 'player_history': dict(history=player.in_all_rounds())}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [P1_PADecision, PlayerBWaitPage, P1_PBDecision, PayoffWaitPage, P2_FinalScreen]
