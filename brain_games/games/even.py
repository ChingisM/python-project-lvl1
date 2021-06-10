import random

# Description for the brain-game engine.
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Return True if argument is even."""
    number %= 2
    answer = True if number == 0 else False
    return answer


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return (question,
            answer)
