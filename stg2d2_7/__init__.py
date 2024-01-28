from otree.api import *
import random as r


doc = """
Stage 2 Decision 2 Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2d2_7'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    # Timeout seconds
    decision_time = None
    feedback_time = None

    # Defining "Advisor" role
    pa_ROLE = 'Advisor'

    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

    # Decision Payoff dictionaries
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300},
        3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300},
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


def is_displayed_pa(player: Player):
    # Is displayed function for role Player A
    return player.role == C.pa_ROLE


def is_displayed_pb(player: Player):
    # Is displayed function for role Player B
    return player.role != C.pa_ROLE


def custom_export(players):
    # header rows
    yield ['session', 'participant_code', 'player_id', 'role', 'treatment', 'decision_number', 'actual_signal', 'payoff', 'low_advice', 'high_advice', 'random_draw', 'max_outside_option']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, participant.PlayerID, participant.role, p.group.treatment, 2, p.group.actual_signal, p.payoff, p.pa_low_advice, p.pa_high_advice, p.random_draw, p.pb_outside_option]


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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.pa_low_advice = r.choice(['Invest', 'Keep'])
            player.pa_high_advice = r.choice(['Invest', 'Keep'])


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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.pb_outside_option = r.randint(0,300)


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


class BeforeNextDecision(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        for player in subsession.get_players():
            signal = player.group.actual_signal
            if player.role != C.pa_ROLE:
                player.participant.vars['D2'] = {'payoff': player.payoff, 'signal': signal,
                                                 'advice': player.group.pa_advice, 'draw': player.random_draw,
                                                 'decision': player.pb_decision(),
                                                 'other_investors': player.other_investors(),
                                                 'investors': player.group.total_players_invest(),
                                                 'pa_payoff': player.group.pa_payoff()}
            else:
                player.participant.vars['D2'] = {'payoff': player.payoff, 'signal': signal, 'advice': player.group.pa_advice,
                                                 'investors': player.group.total_players_invest(),
                                                 'pb_payoff': player.group.pb_payoff()}


page_sequence = [P1_PADecision, PlayerBWaitPage, P1_PBDecision, PayoffWaitPage, BeforeNextDecision]
