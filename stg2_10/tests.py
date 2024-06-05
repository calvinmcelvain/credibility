from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        gend = ['Male', 'Female', 'Transgender', 'Nonbinary', 'Other', 'PNA']
        eth = ['White', 'Asian', 'Native Hawaiian or Pacific Islander', 'Hispanic or Latino', 'African-American', 'Native American', 'Other', 'PNA']
        hispanic = ['Yes', 'No']
        if self.player.role != 'Advisor':
            yield Submission(P1_PBDecision, dict(pb_outside_option=r.randint(1,400)), check_html=False)
        yield Submission(P2_FinalScreen, check_html=False)
        yield Submission(P3_Demographics, dict(age=r.randint(1,99), gender=r.choice(gend), ethnicity=r.choice(eth), hol=r.choice(hispanic)), check_html=False)
        yield Submission(P4_End, check_html=False)
        