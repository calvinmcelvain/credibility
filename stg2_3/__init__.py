from otree.api import *
from settings import INSTRUCTIONS_TIME
import random as r

doc = """
Stage 2 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'stg2_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = INSTRUCTIONS_TIME
    
    # Defining "Advisor" role
    pa_ROLE = 'Advisor'
    
    # Signal decoder
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}

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
    treatment = models.StringField()


class Player(BasePlayer):
    # Sample Decision fields for Player A and B
    pa_low_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)
    pb_outside_option = models.IntegerField(blank=False, min=0, max=400)
    random_draws = models.LongStringField()
    random_investors = models.LongStringField()

    def get_random_draws(self):
        list_of_draws = [r.randint(0, 400) for _ in range(20)]  # Generate 20 random draws
        return f'{list_of_draws}'
    
    
    def get_random_investors(self):
        list_of_investors = [r.randint(1, 4) for _ in range(20)]  # Generate 20 random investor counts
        return f'{list_of_investors}'



# Functions
def creating_session(subsession):
    # Retrieving group matrix from Stage 1
    subsession.set_group_matrix(subsession.session.vars['group_matrix'])
    # Assigning Treatments
    groups = subsession.get_groups()
    treatments = ['LCLE', 'LCHE', 'HCLE', 'HCHE']
    for i, group in enumerate(groups):
        group.treatment = treatments[i % len(treatments)]



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
        return {'pa_table': C.pa_payoff_sample, 'pb_table': C.pb_payoff_sample}
    
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.random_draws = player.get_random_draws()
        player.random_investors = player.get_random_investors()
    
    

class P10(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        cleaned_random_draws = player.random_draws.replace('[', '').replace(']', '')
        random_draws = list(int(x) for x in cleaned_random_draws.split(','))
        cleaned_random_investors = player.random_investors.replace('[', '').replace(']', '')
        investors_rand = list(int(x) for x in cleaned_random_investors.split(','))
        invest_payoff = []
        keep_payoff = []
        investors = []
        advisor_payoff = []
        for i in random_draws:
            if 300 > i:
                investors.append(investors_rand[len(investors)])
                invest_payoff.append(C.pb_payoff_sample[C.decoder['Low']][investors_rand[len(investors)-1] + 1])
                advisor_payoff.append(C.pa_payoff_sample[C.decoder['Low']][investors_rand[len(investors)-1] + 1])
                if 200 > i:
                    keep_payoff.append(C.pb_payoff_sample[C.decoder['Low']][investors_rand[len(investors)-1] + 1])
                else:
                    keep_payoff.append(i)
            else:
                investors.append(investors_rand[len(investors)])
                advisor_payoff.append(C.pa_payoff_sample[C.decoder['Low']][investors_rand[len(investors)-1]])
                invest_payoff.append(i)
                keep_payoff.append(i)

        # Creating a dictionary where draw numbers are keys and a list of corresponding values
        draw_dict = {
            i: {1: random_draws[i], 2: invest_payoff[i], 3: keep_payoff[i], 4: investors[i], 5: advisor_payoff[i]}
            for i in range(20)
        }

        return {'draw_dict': draw_dict, 'invest_value': 250, 'quality': 'Low', 'advice': 'Invest', 'endowment': 300}
    
    
class P11(BaseReadyPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {'history': player.participant.vars['STG1_history']}


class P12(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P13(BaseReadyPage):
    @staticmethod
    def vars_for_template(player):
        return {'pa_table': C.pa_payoff, 'pb_table': C.pb_payoff}


class P14(BaseReadyPage):
    pass


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14]
