from otree.api import *
from settings import INSTRUCTIONS_TIME

doc = """
Stage 2 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = INSTRUCTIONS_TIME

    # Decision Payoff dictionaries
    pb_payoff = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 300, 2: 300, 3: 300, 4: 300, 5: 300},
    }
    pa_payoff = {
        1: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300},
        3: {0: 0, 1: 60, 2: 120, 3: 180, 4: 240, 5: 300}
    }
    
    # Sample Decision Payoff dictionaries
    pb_payoff_sample = {
        1: {1: 400, 2: 0, 3: 400, 4: 0, 5: 400},
        3: {1: 0, 2: 400, 3: 0, 4: 400, 5: 0},
    }
    pa_payoff_sample = {
        1: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400},
        3: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    # Sample Decision fields for Player A and B
    pa_low_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)
    pb_outside_option = models.IntegerField(blank=False, min=0, max=300)
    
    random_draws = models.LongStringField()
    selected_draw = models.IntegerField(initial=51)
    selected_draw_number = models.IntegerField()
    invest_value = models.IntegerField(initial=51)

    def get_random_draws(self):
        list_of_draws = [r.randint(0, 50) for _ in range(20)]  # Generate 20 random draws
        return f'{list_of_draws}'


# PAGES
# Conditional base page
class BaseReadyPage(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}

    

class P1(BaseReadyPage):
    pass


class P2(BaseReadyPage):
    pass


class P3(BaseReadyPage):
    pass


class P4(BaseReadyPage):
    pass


class P5(BaseReadyPage):
    pass


class P6(BaseReadyPage):
    pass


class P7(BaseReadyPage):
    pass


class P8(BaseReadyPage):
    form_model = 'player'
    form_fields = ['pa_low_advice', 'pa_high_advice']
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'pa_table': C.pa_payoff_sample, 'pb_table': C.pb_payoff_sample}
    

class P9(BaseReadyPage):
    form_model = 'player'
    form_fields = ['pb_outside_option']
    
    @staticmethod
    def vars_for_template(player):
        if player.invest_value > 50:
            player.invest_value = r.randint(0, 50)
            invest_value = player.invest_value
        else:
            invest_value = player.invest_value
        player.random_draws = player.get_random_draws()
        cleaned_random_draws = player.random_draws.replace('[', '').replace(']', '')
        random_draws = [int(x) for x in cleaned_random_draws.split(',')]
        player.selected_draw = r.choice(random_draws)
        player.selected_draw_number = random_draws.index(player.selected_draw) + 1
        return {'invest_value': invest_value, 'round_number': player.round_number, 'pa_table': C.pa_payoff_sample, 'pb_table': C.pb_payoff_sample}
    
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number > 2:
            if player.pb_outside_option > player.selected_draw:
                player.payoff = player.invest_value
            else:
                player.payoff = player.selected_draw
    
    

class P10(BaseReadyPage):
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
        for i in random_draws:
            if player.pb_outside_option > i:
                payoffs.append(player.invest_value)
                if player.invest_value >= i:
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

        return {'draw_dict': draw_dict, 'invest_value': player.invest_value, 'round_number': player.round_number}
    
    
class P11(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'history': player.participant.vars['STG1_history']}


class P12(BaseReadyPage):
    pass


class P13(BaseReadyPage):
    pass


class P14(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14]
