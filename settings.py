from os import environ

grouping = 5
participants = 5


# Timeout Seconds
DECISION_TIME = 20000   # In milliseconds (a javascript timeout)
FEEDBACK_TIME = 30  # In seconds
INSTRUCTIONS_TIME = None

SESSION_CONFIGS = [
    dict(
        name='full_experiment',
        display_name='Full Experiment',
        app_sequence=['start', 'stg1_1', 'stg1_2', 'stg2_3', 'stg2_4', 'stg2_5', 'stg2_6', 'stg2_7', 'stg2_8', 'stg2_9', 'stg2_10'],
        num_demo_participants=participants,
    ),
    dict(
        name='experimenter_page',
        display_name='ADMIN: Instructions Page',
        app_sequence=['__admin_exp'],
        num_demo_participants=1,
    ),
]

ROOMS = [
    dict(
        name='lab',
        display_name='lab',
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.04, participation_fee=5.00, doc=""
)

POINTS_CUSTOM_NAME = 'ECU'

PARTICIPANT_FIELDS = ['role', 'STG1_payoff', 'STG1_history', 'D1', 'D2', 'D3', 'PlayerID']
SESSION_FIELDS = ['group_matrix']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6393989826314'