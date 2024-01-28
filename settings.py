from os import environ

demo_instructions = 6
demo_game = 6
demo_final = 6

SESSION_CONFIGS = [
    dict(
        name='Stage_1_Instructions_Only',
        display_name="Stage 1 Instructions (Only)",
        app_sequence=['1_start', '2_stg1instr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_1_Game_Only',
        display_name='Stage 1 Game (Only)',
        app_sequence=['1_start', '3_stg1game'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_1',
        display_name='Stage 1',
        app_sequence=['1_start', '2_stg1instr', '3_stg1game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Instructions_Only',
        display_name='Stage 2 Instructions (Only)',
        app_sequence=['1_start', '4_stg2instr', '5_stg2sldr', '6_stg2d1instr', '8_stg2d2instr', '10_stg2d3instr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Decision_1_Instructions_Only',
        display_name='Stage 2: Decision 1 Instructions (Only)',
        app_sequence=['1_start', '6_stg2d1instr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_1_Game_Only',
        display_name='Stage 2: Decision 1 Game (Only)',
        app_sequence=['1_start', '7_stg2d1game'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_1',
        display_name='Stage 2: Decision 1',
        app_sequence=['1_start', '6_stg2d1instr', '7_stg2d1game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Decision_2_Instructions_Only',
        display_name='Stage 2: Decision 2 Instructions (Only)',
        app_sequence=['1_start', '8_stg2d2instr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_2_Slider',
        display_name='Stage 2: Slider Training',
        app_sequence=['1_start', '5_stg2sldr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_2_Game_Only',
        display_name='Stage 2: Decision 2 Game (Only)',
        app_sequence=['1_start', '9_stg2d2game'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_2',
        display_name='Stage 2: Decision 2',
        app_sequence=['1_start', '8_stg2d2instr', '9_stg2d2game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Decision_3_Instructions_Only',
        display_name='Stage 2: Decision 3 Instructions (Only)',
        app_sequence=['1_start', '10_stg2d3instr'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_3_Game_Only',
        display_name='Stage 2: Decision 3 Game (Only)',
        app_sequence=['1_start', '11_stg2d3game'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_3',
        display_name='Stage 2: Decision 3',
        app_sequence=['1_start', '10_stg2d3instr', '11_stg2d3game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Games',
        display_name='Stage 2 Games (Only)',
        app_sequence=['1_start', '7_stg2d1game', '9_stg2d2game',
                      '11_stg2d3game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2',
        display_name='Stage 2',
        app_sequence=['1_start', '4_stg2instr', '5_stg2sldr', '6_stg2d1instr', '7_stg2d1game', '8_stg2d2instr', '9_stg2d2game', '10_stg2d3instr', '11_stg2d3game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_1_Stage_2',
        display_name='Lab Ready (Stage 1 & 2)',
        app_sequence=['1_start', '2_stg1instr', '3_stg1game', '4_stg2instr', '5_stg2sldr', '6_stg2d1instr', '7_stg2d1game', '8_stg2d2instr', '9_stg2d2game', '10_stg2d3instr', '11_stg2d3game'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='test',
        display_name='test',
        app_sequence=['1_start', '3_stg1game', '7_stg2d1game', '9_stg2d2game', '11_stg2d3game'],
        num_demo_participants=demo_final,
    ),
]

ROOMS = [
    dict(
        name='lab',
        display_name='lab',
        participant_label_file='_rooms/lab',
        use_secure_urls=False
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.04, participation_fee=10.00, doc=""
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