from otree.api import *
import random as r

doc = """
Slider Training
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG2_BGN_SLDR'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

    decision_time = None    # Timeout seconds for decision page
    feedback_time = None    # Timeout seconds for feedback page


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    round_towards_payment = models.IntegerField()
    pb_outside_option = models.IntegerField(blank=False, min=0, max=300)
    random_draws = models.LongStringField()
    selected_draw = models.IntegerField(initial=301)
    selected_draw_number = models.IntegerField()
    invest_value = models.IntegerField(initial=301)

    def get_random_draws(self):
        list_of_draws = [r.randint(0, 300) for _ in range(20)]  # Generate 20 random draws
        return f'{list_of_draws}'


# Functions
def creating_session(subsession):
    players = subsession.get_players()
    for player in players:
        player.round_towards_payment = r.randint(1, 5)


# Custom data export for this game
def custom_export(players):
    # header rows
    yield ['session', 'participant_code', 'player_id', 'role', 'round_number', 'invest_signal', 'max_outside_option']
    for p in players:
        participant = p.participant
        session = p.session
        yield [session.code, participant.code, participant.PlayerID, participant.role, p.round_number, p.selected_draw,p.pb_outside_option]



# PAGES
class P1_Decision(Page):
    form_model = 'player'
    form_fields = ['pb_outside_option']
    timeout_seconds = C.decision_time

    @staticmethod
    def vars_for_template(player):
        if player.invest_value == 301:
            player.invest_value = r.randint(0, 300)
            invest_value = player.invest_value
        else:
            invest_value = player.invest_value
        player.random_draws = player.get_random_draws()
        cleaned_random_draws = player.random_draws.replace('[', '').replace(']', '')
        random_draws = [int(x) for x in cleaned_random_draws.split(',')]
        player.selected_draw = r.choice(random_draws)
        player.selected_draw_number = random_draws.index(player.selected_draw) + 1
        return {'invest_value': invest_value}

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number == player.in_round(1).round_towards_payment:
            if player.pb_outside_option > player.selected_draw:
                player.payoff = player.invest_value
                player.participant.vars['SLDR_payoff'] = player.invest_value
            else:
                player.payoff = player.selected_draw
                player.participant.vars['SLDR_payoff'] = player.selected_draw


class P2_Feedback(Page):
    timeout_seconds = C.feedback_time

    @staticmethod
    def vars_for_template(player):
        cleaned_random_draws = player.random_draws.replace('[', '').replace(']', '')
        random_draws = list(int(x) for x in cleaned_random_draws.split(','))
        draw_numbers = list(range(1, 21))
        payoffs = []
        alt_payoffs = []
        payoff_diff = []
        sign = []
        min_worse = 0
        if player.pb_outside_option > player.invest_value:
            choice_over_alt = 'above'
        elif player.pb_outside_option == player.invest_value:
            choice_over_alt = 'at'
        else:
            choice_over_alt = 'below'
        for i in random_draws:
            if player.pb_outside_option > i:
                payoffs.append(player.invest_value)
                if player.invest_value > i:
                    alt_payoffs.append(player.invest_value)
                    payoff_diff.append(0)
                    sign.append(2)
                else:
                    alt_payoffs.append(i)
                    payoff_diff.append(abs(i - player.invest_value))
                    sign.append(0)
                    min_worse += 1
            else:
                payoffs.append(i)
                if player.invest_value > i:
                    alt_payoffs.append(player.invest_value)
                    payoff_diff.append(abs(i - player.invest_value))
                    sign.append(0)
                    min_worse += 1
                else:
                    alt_payoffs.append(i)
                    payoff_diff.append(0)
                    sign.append(2)

        # Creating a dictionary where draw numbers are keys and a list of corresponding values
        draw_dict = {
            draw_numbers[i]: {1: draw_numbers[i], 2: random_draws[i], 3: payoffs[i], 4: alt_payoffs[i], 5: payoff_diff[i], 6: sign[i]}
            for i in range(len(draw_numbers))
        }

        return {'draw_dict': draw_dict, 'worse': min_worse, 'choice': choice_over_alt, 'invest_value': player.invest_value}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P3_Feedback(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 5

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    @staticmethod
    def vars_for_template(player):
        random_draw = player.in_round(player.in_round(1).round_towards_payment).selected_draw
        outside_option = player.in_round(player.in_round(1).round_towards_payment).pb_outside_option
        payoff = player.in_round(player.in_round(1).round_towards_payment).payoff
        return {'random_draw': random_draw, 'outside_option': outside_option, 'payoff': payoff}


page_sequence = [P1_Decision, P2_Feedback, P3_Feedback]
