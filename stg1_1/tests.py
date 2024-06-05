from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield P1, dict(player_id=1)
        yield Submission(P2, check_html=False)
        yield Submission(P3, check_html=False)
        yield Submission(P4, check_html=False)
        yield Submission(P5, check_html=False)
        yield Submission(P6, check_html=False)
        yield Submission(P7, check_html=False)
        yield Submission(P8, check_html=False)
        yield Submission(P9, check_html=False)
        yield Submission(P10, dict(pa_low_advice='Invest', pa_med_advice='Keep', pa_high_advice='Keep'), check_html=False)
        yield Submission(P11, check_html=False)
        yield Submission(P12, dict(pb_decision='Invest'), check_html=False)
        yield Submission(P13, check_html=False)
        yield Submission(P14, check_html=False)
        yield Submission(P15, check_html=False)
        yield Submission(P16, check_html=False)