"""
game_engine.py

This module handles the core game logic for Nerdle.
It manages the game state, validates user input, and provides feedback.
"""

########################################
# TODO: Import the appropriate modules #
########################################

import equation_generator


###########################################
# ✅ Implemented Function Below #
###########################################

def is_valid_guess(guess):
    if not isinstance(guess, str):
        return False

    if len(guess) != 8:
        return False

    valid_chars = get_valid_characters()
    if not all(char in valid_chars for char in guess):
        return False

    if guess.count('=') != 1:
        return False

    if not equation_generator.validate_equation(guess):
        return False

    return True


################################################################################
#  DO NOT EDIT BELOW THIS LINE, THESE FUNCTIONS ARE ALREADY COMPLETED FOR YOU  #
################################################################################

# ANSI color codes for terminal background colors
COLOR_GREEN = '\033[42m\033[30m'    # Green background, black text
COLOR_YELLOW = '\033[43m\033[30m'   # Yellow background, black text  
COLOR_GRAY = '\033[47m\033[30m'     # Light gray background, black text
COLOR_RESET = '\033[0m'             # Reset to default colors

def create_new_game(target_equation):
    game_state = {
        'target': target_equation,
        'guesses': [],
        'feedback': [],
        'attempts': 0,
        'max_attempts': 6,
        'game_over': False,
        'won': False
    }
    return game_state

def get_feedback(guess, target):
    if len(target) != len(guess):
        return ['B'] * len(guess)
    
    feedback = []
    target_chars = list(target)
    guess_chars = list(guess)
    
    # First pass: mark all exact matches (Green)
    for i in range(len(guess_chars)):
        if i < len(target_chars) and guess_chars[i] == target_chars[i]:
            feedback.append('G')
            target_chars[i] = None
            guess_chars[i] = None
        else:
            feedback.append(None)
    
    # Second pass: mark characters in wrong positions (Yellow)
    for i in range(len(guess_chars)):
        if guess_chars[i] is not None:
            if guess_chars[i] in target_chars:
                feedback[i] = 'Y'
                target_chars[target_chars.index(guess_chars[i])] = None
            else:
                feedback[i] = 'B'
    
    return feedback

def format_feedback_display(guess, feedback):
    display_parts = []
    for i in range(len(guess)):
        char = guess[i] 
        color = feedback[i]
        if color == 'G':
            display_parts.append(f"{COLOR_GREEN} {char} {COLOR_RESET}")
        elif color == 'Y':
            display_parts.append(f"{COLOR_YELLOW} {char} {COLOR_RESET}")
        else:
            display_parts.append(f"{COLOR_GRAY} {char} {COLOR_RESET}")
    return "".join(display_parts)

def format_feedback_plain(guess, feedback):
    display_parts = []
    for i in range(len(guess)):
        char = guess[i] 
        color = feedback[i]
        display_parts.append(f"[{char}{color}]")
    return "".join(display_parts)

def process_guess(game_state, guess):
    if game_state['game_over']:
        return game_state, "Game is already over!"
    
    if not is_valid_guess(guess):
        return game_state, "Invalid guess! Must be exactly 8 characters, mathematically correct equation."
    
    feedback = get_feedback(guess, game_state['target'])
    game_state['guesses'].append(guess)
    game_state['feedback'].append(feedback)
    game_state['attempts'] += 1
    
    if all(color == 'G' for color in feedback):
        game_state['won'] = True
        game_state['game_over'] = True
        message = f"Congratulations! You guessed it in {game_state['attempts']} attempts!"
    elif game_state['attempts'] >= game_state['max_attempts']:
        game_state['game_over'] = True
        message = f"Game over! The equation was: {game_state['target']}"
    else:
        remaining = game_state['max_attempts'] - game_state['attempts']
        message = f"Try again! {remaining} attempts remaining."
    
    return game_state, message

def is_game_over(game_state):
    return game_state['game_over']

def display_game_state(game_state):
    if not game_state['guesses']:
        return "No guesses yet. Make your first guess!"
    
    display_lines = ["Your guesses so far:", ""]
    for i in range(len(game_state['guesses'])):
        guess = game_state['guesses'][i]
        feedback = game_state['feedback'][i]
        formatted_feedback = format_feedback_display(guess, feedback)
        display_lines.append(f"  {formatted_feedback}")
    
    display_lines.append("")
    remaining = game_state['max_attempts'] - game_state['attempts']
    display_lines.append(f"Attempts remaining: {remaining}")
    return "\n".join(display_lines)

def get_valid_characters():
    return "0123456789+-*/="


###########################################
# ✅ Optional Testing Section (for debugging)
###########################################
if __name__ == "__main__":
    # Example manual tests
    test_guesses = [
        "12+34=46",  # ✅ valid
        "1+2=3",     # ❌ too short
        "12+3A=45",  # ❌ invalid char
        "12+34==46", # ❌ double '='
        "12+34=40"   # ❌ invalid equation
    ]

    for guess in test_guesses:
        print(f"{guess} -> {is_valid_guess(guess)}")
