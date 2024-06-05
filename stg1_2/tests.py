from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        mylist = ['Invest', 'Keep']
        if self.player.role == 'Advisor':
            yield Submission(P1_PADecision, dict(pa_low_advice=r.choice(mylist), pa_med_advice=r.choice(mylist), pa_high_advice=r.choice(mylist)), check_html=False)
        else:
            yield Submission(P1_PBDecision, dict(pb_decision=r.choice(mylist)), check_html=False)
        yield Submission(P2_BetweenWaitPage, check_html=False)
        yield Submission(P3_Feedback, check_html=False)