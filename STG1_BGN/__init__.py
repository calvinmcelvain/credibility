from otree.api import *


doc = """
Stage STG1_GAME Instructions App 
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG1_BGN'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = None
    quiz_time = None
    standby_time = None

    # Stage 1 Payoff dictionaries & Player B endowment
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
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    # ID Field
    player_id = models.IntegerField(blank=False, label='')


# PAGES
class P1(Page):
    form_model = 'player'
    form_fields = ['player_id']
    timeout_seconds = C.instructions_time

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        id = player.player_id
        player.participant.vars['PlayerID'] = id


class P2(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P3(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P4(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P5(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P6(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P7(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P8(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P9(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P10(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P11(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P12(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P13(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P14_Quiz(Page):
    timeout_seconds = C.quiz_time

    @staticmethod
    def vars_for_template(player: Player):
        pb_payoff_table = {key: list(value.values()) for key, value in C.pb_payoff.items()}
        pa_payoff_table = {key: list(value.values()) for key, value in C.pa_payoff.items()}
        return {'pa_table': pa_payoff_table, 'pb_table': pb_payoff_table}


class P15_standby(Page):
    timeout_seconds = C.standby_time

    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.vars['role'] == 'Player A':
            return {'role': 'Player A'}
        else:
            return {'role': 'Player B'}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14_Quiz, P15_standby]
