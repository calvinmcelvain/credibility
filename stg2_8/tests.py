from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        mylist = ['Invest', 'Keep']
        if self.player.role == 'Advisor':
            yield Submission(P1_PADecision, dict(pa_low_advice=r.choice(mylist), pa_high_advice=r.choice(mylist)), check_html=False)
        else:
            yield Submission(P1_PBDecision, dict(pb_outside_option=r.randint(1, 400)), check_html=False)