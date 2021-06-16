import random

# Description for the brain-game engine.
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Return True if argument is even."""
    number %= 2
    return number == 0


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_even(number) else 'no'
    return (question,
            answer)
