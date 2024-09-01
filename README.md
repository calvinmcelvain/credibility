# Credibility Experiment

## Description of Apps

1. "*start*"

    - **Initial app** in all session configs

    **Uses:**
    - Functions as the initial session wait-room
    - Sets and stores group matrix and player roles in session/participant fields (**NEEDED**)

2. "*stg1_1*"

- **Stage 1 instructions app**
- No grouping in this app to allow for conditional continue buttons
  - That is, no participant can continue to the next page until all participants in the session have pressed the continue button
  - **Note:** The reason for instruction and game app separation is due to the conditional continue buttons
    - oTree's custom websocket, "Live Pages/Method", only sends information to the group level, therefore the continue buttons in seperated groups would only allow the last group to continue and not the entire session

- "*stg1_2*"

  - **Stage 1 app**
  - Consist of 30 rounds
  - Groups of 5
  - 2 player roles: Advisor and Investor
    - Only 'Advisor' is defined because oTree only allows 1 role per player
  - 4 treatments
    - Defined and set in the "creating_session" function
  - 1 page per player decision, a between 'waitpage', and a feedback page

- "*stg2_1*"

  - **Stage 2 and scenario 1 instructions app**
  - Same conditional continue button as Stage 1 Instructions
  - No quiz

- "*stg2_2*"

  - **Stage 2 scenario 1 app**
  