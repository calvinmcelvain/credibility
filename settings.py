from os import environ

# Session settings (time, groups, rounds)
GROUPING = 2
STAGE_1_ROUNDS = 5
DECISION_TIME = 20000   # In milliseconds (a javascript timeout)
FEEDBACK_TIME = None  # In seconds
INSTRUCTIONS_TIME = None
SKIP = True

# Demo participants
participants = 2

SESSION_CONFIGS = [
    dict(
        name='Stage_1_Instructions_Only',
        display_name="Stage 1: Instructions",
        app_sequence=['start', 'stg1_1'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_1_Game_Only',
        display_name='Stage 1: Game',
        app_sequence=['start', 'stg1_2'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_1',
        display_name='Stage 1',
        app_sequence=['start', 'stg1_1', 'stg1_2'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Scenario_1',
        display_name='Stage 2: Scenario 1',
        app_sequence=['start', 'stg2_1', 'stg2_2'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Scenario_2',
        display_name='Stage 2: Scenario 2',
        app_sequence=['start', 'stg2_3', 'stg2_4'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Scenario_3',
        display_name='Stage 2: Scenario 3',
        app_sequence=['start', 'stg2_5', 'stg2_6'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Scenario_4',
        display_name='Stage 2: Scenario 4',
        app_sequence=['start', 'stg2_7', 'stg2_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Instructions_Only',
        display_name='Stage 2: Instructions',
        app_sequence=['start', 'stg2_1', 'stg2_3', 'stg2_5', 'stg2_7'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Games',
        display_name='Stage 2: All Scenarios',
        app_sequence=['start', 'stg2_2', 'stg2_4',
                      'stg2_6', 'stg2_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2',
        display_name='Stage 2',
        app_sequence=['start', 'stg2_1', 'stg2_2', 'stg2_3', 'stg2_4', 'stg2_5', 'stg2_6', 'stg2_7', 'stg2_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_1_Stage_2',
        display_name='Full Experiment',
        app_sequence=['start', 'stg1_1', 'stg1_2', 'stg2_1', 'stg2_2', 'stg2_3', 'stg2_4', 'stg2_5', 'stg2_6', 'stg2_7', 'stg2_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='experimenter_page',
        display_name='Admin: Experiment Instructions',
        app_sequence=['admin_start', 'stg1_1', 'stg2_1', 'stg2_3', 'stg2_5', 'stg2_7'],
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
    real_world_currency_per_point=0.04, 
    participation_fee=5.00, 
    doc=""
)

POINTS_CUSTOM_NAME = 'ECU'

PARTICIPANT_FIELDS = ['role', 'stage_1_payoff', 'stage_1_history', 'scenario_1_history', 'scenario_2_history', 'scenario_3_history']
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

DEMO_PAGE_INTRO_HTML = """
Git Branch: lab_testing
"""

SECRET_KEY = '6393989826314'