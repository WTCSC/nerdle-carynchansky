# **Nerdle** – The Math Equation Guessing Game
## Overview

**Nerdle** is a Python-based math puzzle game inspired by Wordle, but with numbers and equations! Your goal is to guess the hidden 8-character equation (like 12+34=46) in 6 tries or fewer. After each guess, you’ll get color-coded feedback that tells you how close you are.

## Features

- Randomly generated math equations (+, -, *, /)
- Fully validated math logic (no fake equations!)
- 6 attempts per round
- Color-coded feedback system (Green, Yellow, Gray)
- Smart equation validation and input checking
- Play as many rounds as you want

## How the Game Works

1. The game randomly creates a valid 8-character equation such as:
   * 12+34=46
2. You have 6 tries to guess the correct equation.

3. After each guess:

   * Green: Correct character in the correct position

   * Yellow: Correct character in the wrong position

   * Gray: Character not in the equation

4. You win if your equation matches the target exactly!

5. If you run out of attempts, the correct equation is revealed.

## How to Play
1. Clone the repository:
   
   **git clone name_of_repository**
2. Run the game:

   **Make sure you’re in the same directory as the Python files, then run:**

   **python3 nerdle.py**

## Requirements:

Python 3.7 or newer

No external libraries needed (only built-in modules)

## Desicion Tree:
![Decision Tree](<Screenshot from 2025-10-09 10-01-30.png>)
![Desicion Tree](<Screenshot from 2025-10-09 10-01-43.png>)

