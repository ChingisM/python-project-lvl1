import random

# Description for the brain-game engine.
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Return True if argument is prime."""
    if number <= 1:
        return False
    i = 2
    while number % i != 0:
        i += 1
    return i == number


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    number = random.randint(-5, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return (question,
            answer)
