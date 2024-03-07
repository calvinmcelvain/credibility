from otree.api import *
import random as r

from settings import grouping, DECISION_TIME, FEEDBACK_TIME

doc = """
Stage 2 Decision 3 Game & Final Payoff screen
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2d3_9'
    PLAYERS_PER_GROUP = grouping
    NUM_ROUNDS = 1

    # Timeout seconds

    decision_time = DECISION_TIME
    feedback_time = FEEDBACK_TIME

    # Defining "Advisor" role
    pa_ROLE = 'Advisor'

    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

    # Decision Payoff dictionaries
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300}
    }
    pa_payoff = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Group treatment field
    treatment = models.StringField()

    # Randomly drawn fields
    actual_signal = models.StringField()
    pa_advice = models.StringField()
    decision_towards_payment = models.IntegerField()

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
        return sum(1 for player in self.get_players() if player.role != C.pa_ROLE and player.pb_outside_option > player.random_draw)


class Player(BasePlayer):
    # Decision fields for Player A and B
    pa_low_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)
    pb_outside_option = models.IntegerField(blank=False, min=0, max=300)
    random_draw = models.IntegerField(min=0, max=300)

    # Player history functions meant to be passed to template in feedback page
    def other_investors(self):
        if self.role != C.pa_ROLE and self.pb_outside_option > self.random_draw:
            others = (self.group.total_players_invest() - 1)
            return others
        else:
            return self.group.total_players_invest()

    def pb_decision(self):
        if self.role != C.pa_ROLE:
            if self.pb_outside_option > self.random_draw:
                return 'Invest'
            else:
                return "Keep"


# Functions
def creating_session(subsession):
    # Retrieving group matrix from Stage 1
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])

    # Assigning Treatments
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


def is_displayed_pa(player: Player):
    # Is displayed function for role Player A
    return player.role == C.pa_ROLE


def is_displayed_pb(player: Player):
    # Is displayed function for role Player B
    return player.role != C.pa_ROLE


def custom_export(players):
    # header rows
    yield ['session', 'participant_code', 'player_id', 'role', 'treatment', 'decision_number', 'actual_signal', 'payoff', 'payoff_counts', 'low_advice', 'high_advice', 'random_draw', 'max_outside_option']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, participant.PlayerID, participant.role, p.group.treatment, 1, p.group.actual_signal, p.payoff, p.group.decision_towards_payment, p.pa_low_advice, p.pa_high_advice, p.random_draw, p.pb_outside_option]


# PAGES
class P1_PADecision(Page):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_high_advice']
    timeout_seconds = C.decision_time
    is_displayed = is_displayed_pa

    @staticmethod
    def vars_for_template(player: Player):
        signal = player.group.actual_signal
        return {'signal': signal, 'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class PlayerBWaitPage(WaitPage):
    body_text = 'Waiting for Player A to give investment advice'
    is_displayed = is_displayed_pb

    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            if player.role != C.pa_ROLE:
                player.random_draw = r.randint(1, 300)


class P1_PBDecision(Page):
    form_model = 'player'
    form_fields = ['pb_outside_option']
    is_displayed = is_displayed_pb
    timeout_seconds = C.decision_time

    @staticmethod
    def vars_for_template(player: Player):
        if player.group.actual_signal == 'High':
            player.group.pa_advice = player.group.get_player_by_role(C.pa_ROLE).pa_high_advice
        else:
            player.group.pa_advice = player.group.get_player_by_role(C.pa_ROLE).pa_low_advice

        return {'advice': player.group.pa_advice, 'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class PayoffWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        # Payoff Dictionaries
        pb_payoff = C.pb_payoff
        pa_payoff = C.pa_payoff
        signal = group.actual_signal

        # Defining payoffs
        decoder = C.decoder
        for player in group.get_players():
            if player.role != C.pa_ROLE:
                if player.pb_outside_option > player.random_draw:
                    player.payoff = pb_payoff[decoder[signal]][group.total_players_invest()]
                else:
                    player.payoff = player.random_draw
            else:
                player.payoff = pa_payoff[decoder[signal]][group.total_players_invest()]


class P2_FinalScreen(Page):
    @staticmethod
    def vars_for_template(player: Player):
        stage1_payoff = player.participant.vars['STG1_payoff']
        SLDR_payoff_raw = player.participant.vars['SLDR_payoff']
        SLDR_payoff = cu(SLDR_payoff_raw)
        D1 = player.participant.vars['D1']['payoff']
        D2 = player.participant.vars['D2']['payoff']
        stage2_payoff_dict = {
            1: D1,
            2: D2,
            3: player.payoff
        }
        stage2_payoff = stage2_payoff_dict[player.group.decision_towards_payment]

        # Calculating Participant payoff (Based on chosen decision)
        remainder = (player.participant.payoff - stage1_payoff - stage2_payoff - SLDR_payoff)
        player.participant.payoff = (player.participant.payoff - remainder)

        final_payoff = stage1_payoff + stage2_payoff + SLDR_payoff
        real_stg1 = stage1_payoff.to_real_world_currency(player.session)
        real_sldr = SLDR_payoff.to_real_world_currency(player.session)
        real_stg2 = stage2_payoff.to_real_world_currency(player.session)
        real_final = final_payoff.to_real_world_currency(player.session)
        final = real_final + 10
        decision_counts = player.group.in_round(1).decision_towards_payment
        history = {
            1: player.participant.vars['D1'],
            2: player.participant.vars['D2'],
            3: player.in_all_rounds()
        }
        return {'final_payoff': final_payoff, 'Stage_1': stage1_payoff, 'Stage_2': stage2_payoff, 'slider_training': SLDR_payoff
                , 'real_final': real_final, 'real_Stage_1': real_stg1, 'real_slider': real_sldr, 'real_Stage_2': real_stg2,
                'final': final, 'decision_counts': decision_counts, 'history': history}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [P1_PADecision, PlayerBWaitPage, P1_PBDecision, PayoffWaitPage, P2_FinalScreen]
