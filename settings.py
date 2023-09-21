from os import environ

SESSION_CONFIGS = [
    dict(
        name='STG1_BGN',
        display_name="STG1_GAME Instructions",
        app_sequence=['START', 'STG1_BGN'],
        num_demo_participants=2,
    ),
    dict(
        name='STG1_GAME',
        display_name="STG1_GAME",
        app_sequence=['START', 'STG1_GAME'],
        num_demo_participants=2,
    ),
    dict(
        name='Stage_1_Final',
        display_name="Final: STG1",
        app_sequence=['START', 'STG1_BGN', 'STG1_GAME'],
        num_demo_participants=2,
    ),
    dict(
        name='STG2_BGN',
        display_name="STG2_GAME Instructions",
        app_sequence=['START', 'STG2_BGN'],
        num_demo_participants=2,
    ),
    dict(
        name='STG2_GAME',
        display_name="STG2_GAME",
        app_sequence=['START', 'STG2_GAME'],
        num_demo_participants=2,
    ),
    dict(
        name='Stage_2_Final',
        display_name="Final: STG2_GAME",
        app_sequence=['START', 'STG2_BGN', 'STG2_GAME'],
        num_demo_participants=2,
    ),
    dict(
        name='Final',
        display_name="Final: STG 1 & 2",
        app_sequence=['START', 'STG1_BGN', 'STG1_GAME', 'STG2_BGN', 'STG2_GAME'],
        num_demo_participants=2,
    ),
    dict(
        name='Final_Games',
        display_name="Final STG 1 & 2 Games",
        app_sequence=['START', 'STG1_GAME', 'STG2_GAME'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.25, participation_fee=10.00, doc=""
)

PARTICIPANT_FIELDS = ['role', 'Stage1_payoff', 'PlayerID']
SESSION_FIELDS = ['group_matrix']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('Crd2')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6393989826314'