import random

# Description for the brain-game engine.
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 2
    while number % i != 0:
        i += 1
    return i == number


def generate_round():
    question = random.randint(2, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return (question,
            answer)
