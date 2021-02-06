import random


def numbers_generating():
    """Return two random generated numbers."""
    num1 = random.randrange(1, 51, 3)
    num2 = random.randrange(1, 51, 3)
    return [num1,
            num2]


def question_generating(num1, num2):
    """Return a formed question for the brain-game engine."""
    question = str(num1) + ' ' + str(num2)
    return question


def determining_gcd(num1, num2):
    """Return a greatest common divisor of two numbers."""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        elif num1 == num2:
            gcd = num1
            return str(gcd)
        else:
            num2 = num2 % num1
    gcd = num1 + num2
    return str(gcd)


def round_generating():
    """Return generated question and answer for a round
    in the brain-game engine."""
    num1, num2 = numbers_generating()
    question = question_generating(num1, num2)
    answer = determining_gcd(num1, num2)
    return [question,
            answer]


# Description for the brain-game engine.
DESCRIPTION = 'Find the greatest common divisor of given numbers.'
