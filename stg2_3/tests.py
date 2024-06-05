from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(P1, check_html=False)
        yield Submission(P2, check_html=False)
        yield Submission(P3, check_html=False)
        yield Submission(P4, check_html=False)
        yield Submission(P5, check_html=False)
        yield Submission(P6, check_html=False)
        yield Submission(P7, check_html=False)
        yield Submission(P8, dict(pa_low_advice2='Invest', pa_high_advice2='Keep'), check_html=False)
        yield Submission(P9, dict(pb_outside_option=300), check_html=False)
        yield Submission(P10, check_html=False)
        yield Submission(P11, check_html=False)
        yield Submission(P12, check_html=False)
        yield Submission(P13, check_html=False)
        yield Submission(P14, check_html=False)