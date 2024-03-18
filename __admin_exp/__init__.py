from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = '__admin_exp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Stage 1 Payoff dictionaries & Investor endowment
    pb_payoff1 = {
        1: {1: 0, 2: 1, 3: 2, 4: 3, 5: 4},
        2: {1: 1, 2: 3, 3: 5, 4: 7, 5: 9},
        3: {1: 2, 2: 4, 3: 8, 4: 14, 5: 22}
    }
    pa_payoff1 = {
        1: {0: 12, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3},
        2: {0: 6, 1: 6, 2: 6, 3: 6, 4: 6, 5: 12},
        3: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 30}
    }
    pb_endowment = 12
    # Decision Payoff dictionaries
    pb_payoff2 = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 300, 2: 300, 3: 300, 4: 300, 5: 300},
    }
    pa_payoff2 = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }
    # Decision Payoff dictionaries
    pb_payoff3 = {
        1: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300},
        3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300},
    }
    pa_payoff3 = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }
    # Decision Payoff dictionaries
    pb_payoff4 = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 0, 2: 0, 3: 300, 4: 300, 5: 300}
    }
    pa_payoff4 = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }



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
class BaseReadyPage1(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff1, 'pb_table': C.pb_payoff1}


class BaseReadyPage2(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff2, 'pb_table': C.pb_payoff2}


class BaseReadyPage3(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff3, 'pb_table': C.pb_payoff3}


class BaseReadyPage4(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff4, 'pb_table': C.pb_payoff4}


class P1(Page):
    form_model = 'player'
    form_fields = ['player_id']


class P2(BaseReadyPage1):
    pass


class P3(BaseReadyPage1):
    pass


class P4(BaseReadyPage1):
    pass


class P5(BaseReadyPage1):
    pass


class P6(BaseReadyPage1):
    pass


class P7(BaseReadyPage1):
    pass


class P8(BaseReadyPage1):
    pass


class P9(BaseReadyPage1):
    pass


class P10(BaseReadyPage1):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_med_advice', 'pa_high_advice']


class P11(BaseReadyPage1):
    pass


class P12(Page):
    form_model = 'player'
    form_fields = ['pb_decision']

    @staticmethod
    def vars_for_template(player: Player):
        advice = 'Invest'
        return {'pa_table': C.pa_payoff1, 'pb_table': C.pb_payoff1, 'advice': advice}


class P13(BaseReadyPage1):
    pass


class P14(BaseReadyPage1):
    pass


class P15(BaseReadyPage1):
    pass


class P17(BaseReadyPage2):
    pass


class P18(BaseReadyPage2):
    pass


class P19(BaseReadyPage2):
    pass


class P20(BaseReadyPage2):
    pass


class P21(BaseReadyPage2):
    pass


class P22(BaseReadyPage2):
    pass


class P23(BaseReadyPage2):
    pass


class P24(BaseReadyPage2):
    pass


class P25(BaseReadyPage2):
    pass


class P26(BaseReadyPage2):
    pass


class P27(BaseReadyPage2):
    pass


class P28(BaseReadyPage3):
    pass


class P29(BaseReadyPage3):
    pass


class P30(BaseReadyPage4):
    pass


class P31(BaseReadyPage4):
    pass


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31]