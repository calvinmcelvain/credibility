from otree.api import *
import random as r

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = '__admin_exp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    decoder = {1: 'Low', 3: 'High', 'Low': 1, 'High': 3}
    # Sample Decision Payoff dictionaries
    pb_payoff_sample = {
        1: {1: 400, 2: 0, 3: 400, 4: 0, 5: 400},
        3: {1: 0, 2: 400, 3: 0, 4: 400, 5: 0},
    }
    pa_payoff_sample = {
        1: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400},
        3: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400}
    }

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
        3: {1: 400, 2: 400, 3: 400, 4: 400, 5: 400},
    }
    pa_payoff2 = {
        1: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400},
        3: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400}
    }
    # Decision Payoff dictionaries
    pb_payoff3 = {
        1: {1: 0, 2: 0, 3: 400, 4: 400, 5: 400},
        3: {1: 0, 2: 0, 3: 400, 4: 400, 5: 400},
    }
    pa_payoff3 = {
        1: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400},
        3: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400}
    }
    # Decision Payoff dictionaries
    pb_payoff4 = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        3: {1: 0, 2: 0, 3: 400, 4: 400, 5: 400}
    }
    pa_payoff4 = {
        1: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400},
        3: {0: 0, 1: 80, 2: 160, 3: 240, 4: 320, 5: 400}
    }



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ID Field
    player_id = models.IntegerField(blank=False, label='', max=99)

    # sample Decision Models
    pb_decision = models.StringField(blank=False)
    pa_low_advice = models.StringField(blank=False)
    pa_med_advice = models.StringField(blank=False)
    pa_high_advice = models.StringField(blank=False)

    def get_random_investors(self):
        investors = [1, 2, 3, 4] * 5
        r.shuffle(investors) 
        return investors



# PAGES
# Conditional Page
class BaseReadyPage1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff1, 'pb_table': C.pb_payoff1}


class BaseReadyPage2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff2, 'pb_table': C.pb_payoff2}


class BaseReadyPage3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff3, 'pb_table': C.pb_payoff3}


class BaseReadyPage4(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # Passing the player payoffs
        return {'pa_table': C.pa_payoff4, 'pb_table': C.pb_payoff4}


class P1(Page):
    pass


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
    pass


class P11(BaseReadyPage1):
    pass


class P12(Page):
    @staticmethod
    def vars_for_template(player: Player):
        advice = 'Invest'
        return {'pa_table': C.pa_payoff1, 'pb_table': C.pb_payoff1, 'advice': advice}


class P13(BaseReadyPage1):
    pass


class P14(BaseReadyPage1):
    pass


class P15(BaseReadyPage2):
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
    @staticmethod
    def vars_for_template(player):
        draws = [250] * 20
        investors_rand = player.get_random_investors()
        invest_payoff = []
        keep_payoff = []
        investors = []
        advisor_payoff = []
        for i in draws:
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
            i: {1: draws[i], 2: invest_payoff[i], 3: keep_payoff[i], 4: investors[i], 5: advisor_payoff[i]}
            for i in range(20)
        }

        return {'draw_dict': draw_dict, 'invest_value': 250, 'quality': 'Low', 'advice': 'Invest', 'endowment': 300}


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


page_sequence = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P17, P18, P19, P20, P21, P22, P23, P24, P26, P27, P28, P29, P30, P31]