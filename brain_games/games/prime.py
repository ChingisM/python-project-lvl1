import random


def question_generating():
    """Return a random generated number."""
    return random.randint(2, 100)


def is_prime(number):
    i = 2
    while number % i != 0:
        i += 1
    return i == number


def round_generating():
    question = question_generating()
    answer = 'yes' if is_prime(question) else 'no'
    return [question,
            answer]


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
