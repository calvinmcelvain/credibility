from os import environ

demo_instructions = 2
demo_game = 2
demo_final = 2

SESSION_CONFIGS = [
    dict(
        name='Stage_1_Instructions_Only',
        display_name="Stage 1 Instructions (Only)",
        app_sequence=['START', 'STG1_BGN'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_1_Game_Only',
        display_name='Stage 1 Game (Only)',
        app_sequence=['START', 'STG1_GAME'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_1',
        display_name='Stage 1',
        app_sequence=['START', 'STG1_BGN', 'STG1_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Decision_1_Instructions_Only',
        display_name='Stage 2: Decision 1 Instructions (Only)',
        app_sequence=['START', 'STG2_BGN', 'STG2_BGN_SLDR', 'STG2_D1_BGN'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_1_Game_Only',
        display_name='Stage 2: Decision 1 Game (Only)',
        app_sequence=['START', 'STG2_D1_GAME'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_1',
        display_name='Stage 2: Decision 1',
        app_sequence=['START', 'STG2_D1_BGN', 'STG2_D1_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Decision_2_Instructions_Only',
        display_name='Stage 2: Decision 2 Instructions (Only)',
        app_sequence=['START', 'STG2_D2_BGN'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_2_Slider',
        display_name='Stage 2: Slider Training',
        app_sequence=['START', 'STG2_BGN_SLDR'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_2_Game_Only',
        display_name='Stage 2: Decision 2 Game (Only)',
        app_sequence=['START', 'STG2_D2_GAME'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_2',
        display_name='Stage 2: Decision 2',
        app_sequence=['START', 'STG2_D2_BGN', 'STG2_D2_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Decision_3_Instructions_Only',
        display_name='Stage 2: Decision 3 Instructions (Only)',
        app_sequence=['START', 'STG2_D3_BGN'],
        num_demo_participants=demo_instructions,
    ),
    dict(
        name='Stage_2_Decision_3_Game_Only',
        display_name='Stage 2: Decision 3 Game (Only)',
        app_sequence=['START', 'STG2_D3_GAME'],
        num_demo_participants=demo_game,
    ),
    dict(
        name='Stage_2_Decision_3',
        display_name='Stage 2: Decision 3',
        app_sequence=['START', 'STG2_D3_BGN', 'STG2_D3_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2_Games',
        display_name='Stage 2 Games (Only)',
        app_sequence=['START', 'STG2_D1_GAME', 'STG2_D2_GAME',
                      'STG2_D3_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_2',
        display_name='Stage 2',
        app_sequence=['START', 'STG2_BGN', 'STG2_BGN_SLDR', 'STG2_D1_BGN', 'STG2_D1_GAME', 'STG2_D2_BGN', 'STG2_D2_GAME', 'STG2_D3_BGN', 'STG2_D3_GAME'],
        num_demo_participants=demo_final,
    ),
    dict(
        name='Stage_1_Stage_2',
        display_name='Stage 1 & Stage 2',
        app_sequence=['START', 'STG1_BGN', 'STG1_GAME', 'STG2_BGN', 'STG2_BGN_SLDR', 'STG2_D1_BGN', 'STG2_D1_GAME', 'STG2_D2_BGN', 'STG2_D2_GAME', 'STG2_D3_BGN', 'STG2_D3_GAME'],
        num_demo_participants=demo_final,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.04, participation_fee=10.00, doc=""
)

PARTICIPANT_FIELDS = ['role', 'STG1_payoff', 'SLDR_payoff', 'D1_payoff', 'D2_payoff', 'PlayerID']
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