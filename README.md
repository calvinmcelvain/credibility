# Credibility Experiment
### Description of Apps:

- "START":

    - Initial app in all session configs
    - Used as a beginning session wait-room
    - Sets and stores group matrix and player roles in session/participant fields

- "STG1_BGN":

    - Stage 1 Instructions
    - No groups in this app to allow for conditional continue buttons
      - That is, no participant can continue to the next page until all participants in the session have pressed the continue button
    - **Note** The reason for instruction adn game seperation is due to the conditional continue buttons
      - oTree's custom websocket, "Live Pages/Method", only sends information to the group level, therefore the continue buttons in seperated groups would only allow the last group to continue and not the entire session

- "STG1_GAME":

  - Stage 1 Game
  - Consist of 30 rounds, groups of 6, 2 player roles (only 'Player A' is defined because oTree only allows 1 role per player)
  - 4 treatments (total of 24 participants per session), defined in C(BaseConstants)
  - 1 page per player decision, a 'between page', and a feedback page
  - Most variables are denoted with pa... pb..., previous identifying roles were Player A/Player B, now are identified as Investor/Advisor, respectively

- "STG2_BGN":

  - Stage 2 Instructions with same conditional continue button as Stage 1 Instructions
  - No quiz

- "STG2_GAME":

  - Stage 2 Game
  - Consist of 3 'rounds' (decisions)
    - Only 1 round counts towards points
  - At the end of the 3 rounds, end of experiment stats/points are shown to participant including participantion fee ($10)