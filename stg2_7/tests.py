from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(P1, check_html=False)
        yield Submission(P2, check_html=False)
        yield Submission(P3, check_html=False)