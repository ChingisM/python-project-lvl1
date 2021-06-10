import random

# Description for the brain-game engine.
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def define_gcd(num1, num2):
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
    return gcd


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    num1, num2 = random.randrange(1, 51, 3), random.randrange(1, 51, 3)
    question = str(num1) + ' ' + str(num2)
    answer = str(define_gcd(num1, num2))
    return (question,
            answer)
