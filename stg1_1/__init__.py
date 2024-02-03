from otree.api import *
from settings import INSTRUCTIONS_TIME


doc = """
Stage Stage 1 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg1_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout Seconds
    instructions_time = INSTRUCTIONS_TIME

    # Stage 1 Payoff dictionaries & Investor endowment
    pb_payoff = {
        1: {1: 0, 2: 1, 3: 2, 4: 3, 5: 4},
        2: {1: 1, 2: 3, 3: 5, 4: 7, 5: 9},
        3: {1: 2, 2: 4, 3: 8, 4: 14, 5: 22}
    }
    pa_payoff = {
        1: {0: 12, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3},
        2: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 12},
        3: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 30}
    }
    pb_endowment = 12


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    # Not passed to data export
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    # ID Field
    player_id = models.IntegerField(blank=False, label='', max=99)

    # sample Decision Models
    pb_decision = models.StringField(blank=False)
    pa_low_advice = models.StringField(blank=False)
    pa_med_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)


# PAGES
# Conditional Page
class BaseReadyPage(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P1(Page):
    form_model = 'player'
    form_fields = ['player_id']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Storing ID to the participant field
        id = player.player_id
        player.participant.vars['PlayerID'] = id


class P2(BaseReadyPage):
    pass


class P3(BaseReadyPage):
    pass


class P4(BaseReadyPage):
    pass


class P5(BaseReadyPage):
    pass


class P6(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P7(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P8(BaseReadyPage):
    pass


class P9(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P10(BaseReadyPage):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_med_advice', 'pa_high_advice']

    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P11(BaseReadyPage):
    form_model = 'player'
    form_fields = ['pb_decision']

    @staticmethod
    def vars_for_template(player: Player):
        advice = 'Invest'
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff, 'advice': advice}


class P12(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P13(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P14(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P15(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        role = 'Advisor' if player.participant.vars['role'] == 'Advisor' else 'Investor'
        return {'role': role}


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15]
