from os import environ

grouping = 2
participants = 2


# Timeout Seconds
DECISION_TIME = 20000   # In milliseconds (a javascript timeout)
FEEDBACK_TIME = None  # In seconds
INSTRUCTIONS_TIME = None

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
        name='Decision_1_Instructions_Only',
        display_name='Stage 2: Decision 1 Instructions',
        app_sequence=['start', 'stg2d1_3'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_1_Game_Only',
        display_name='Stage 2: Decision 1 Game',
        app_sequence=['start', 'stg2d1_4'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_1',
        display_name='Stage 2: Decision 1',
        app_sequence=['start', 'stg2d1_3', 'stg2d1_4'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_2_Instructions_Only',
        display_name='Stage 2: Decision 2 Instructions',
        app_sequence=['start', 'stg2d2_6'],
        num_demo_participants=participants,
    ),

    dict(
        name='Stage_2_Decision_2_Game_Only',
        display_name='Stage 2: Decision 2 Game',
        app_sequence=['start', 'stg2d2_7'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_2',
        display_name='Stage 2: Decision 2',
        app_sequence=['start', 'stg2d2_6', 'stg2d2_7'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_3_Instructions_Only',
        display_name='Stage 2: Decision 3 Instructions',
        app_sequence=['start', 'stg2d3_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_3_Game_Only',
        display_name='Stage 2: Decision 3 Game',
        app_sequence=['start', 'stg2d3_9'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_3',
        display_name='Stage 2: Decision 3',
        app_sequence=['start', 'stg2d3_8', 'stg2d3_9'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Instructions_Only',
        display_name='Stage 2: Instructions',
        app_sequence=['start', 'stg2_1', 'stg2_2', 'stg2d1_3', 'stg2d2_6', 'stg2d3_8'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Decision_2_Slider',
        display_name='Stage 2: Slider Training',
        app_sequence=['start', 'stg2_2'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2_Games',
        display_name='Stage 2: All Decisions',
        app_sequence=['start', 'stg2d1_4', 'stg2d2_7',
                      'stg2d3_9'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_2',
        display_name='Stage 2',
        app_sequence=['start', 'stg2_1', 'stg2_2', 'stg2d1_3', 'stg2d1_4', 'stg2d2_6', 'stg2d2_7', 'stg2d3_8', 'stg2d3_9'],
        num_demo_participants=participants,
    ),
    dict(
        name='Stage_1_Stage_2',
        display_name='Full Experiment',
        app_sequence=['start', 'stg1_1', 'stg1_2', 'stg2_1', 'stg2_2', 'stg2d1_3', 'stg2d1_4', 'stg2d2_6', 'stg2d2_7', 'stg2d3_8', 'stg2d3_9'],
        num_demo_participants=participants,
    ),
    dict(
        name='Slider_page',
        display_name='ADMIN: Slider Page',
        app_sequence=['__admin_slider'],
        num_demo_participants=1,
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
        participant_label_file='_rooms/lab'
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.04, participation_fee=5.00, doc=""
)

POINTS_CUSTOM_NAME = 'ECU'

PARTICIPANT_FIELDS = ['role', 'STG1_payoff', 'STG1_history', 'SLDR_payoff', 'D1', 'D2', 'PlayerID']
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