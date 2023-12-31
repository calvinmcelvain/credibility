# Credibility Experiment
### Description of Apps:

- "START":

    - Initial app in all session configs
    - Used as a beginning session wait-room
    - Sets and stores group matrix and player roles in session/participant fields (NEEDED)

- "STG1_BGN":

    - Stage 1 Instructions
    - No groups in this app to allow for conditional continue buttons
      - That is, no participant can continue to the next page until all participants in the session have pressed the continue button
      - **Note:** The reason for instruction and game separation is due to the conditional continue buttons
        - oTree's custom websocket, "Live Pages/Method", only sends information to the group level, therefore the continue buttons in seperated groups would only allow the last group to continue and not the entire session

- "STG1_GAME":

  - Stage 1 Game
  - Consist of 30 rounds, groups of 6, 2 player roles (only 'Player A' is defined because oTree only allows 1 role per player)
  - 4 treatments for each group (total of 24 participants per session), defined in C(BaseConstants)
  - 1 page per player decision, a 'between page', and a feedback page
  - Most variables are denoted with "pa...", "pb...", previous identifying roles were Player A/Player B, now are identified as Investor/Advisor, respectively

- "STG2_BGN":

  - Stage 2 Instructions with same conditional continue button as Stage 1 Instructions
  - No quiz

- "STG2_BGN_SLDR"

  - Stage 2 Slider training exercise
  - Consists of 10 rounds
    - In each round there are 20 random draws, in which 1 is randomly selected
  - This exercise is meant to get subjects familiar with the slider

- "STG2_D1_BGN"

  - Stage 2 Decision 1 instructions | Conditional continue buttons
  - Stage 2 has 3 separate decisions 

- "STG2_D1_GAME"

  - Stage 2 Decision 1 game

- "STG2_D2_BGN"

  - Stage 2 Decision 2 instructions | Conditional continue buttons

- "STG2_D2_GAME"

  - Stage 2 Decision 2 game

- "STG2_D3_BGN"

  - Stage 2 Decision 3 instructions | Conditional continue buttons

- "STG2_D3_GAME"

  - Stage 2 Decision 3 game
  - At the end of game, the end of experiment feedback page is given
    - In which, participants are shown the feedback from the previous 3 decisions in Stage 2 as well as total ECUs earned and ending $ made  (Including $10 show up fee)