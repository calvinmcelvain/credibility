from otree.api import *


doc = """
Stage 2 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG2_BGN'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    pass


# PAGES
class P1(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P2(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 2
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P3(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 3
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P4(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 4
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P5(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 5
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P6(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 6
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P7(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 7
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P8(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 8
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P9(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 9
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P10(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 10
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class P11(Page):
    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 11
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


class STG2Information(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.vars['role'] == 'Player A':
            return {'role': 'Player A'}
        else:
            return {'role': 'Player B'}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players()) * 12
        if player.group.all_players_ready == players_in_session:
            return {0: 'all_ready'}


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, STG2Information]
