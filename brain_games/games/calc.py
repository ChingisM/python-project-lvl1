import random

# Description for the brain-game engine.
DESCRIPTION = 'What is the result of the expression?'


def calculate_result(num1, num2, operator):
    """Return a result of an arithmetic operation with two numbers."""
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    num1, num2 = random.randint(11, 20), random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = str(num1) + ' ' + operator + ' ' + str(num2)
    answer = str(calculate_result(num1, num2, operator))
    return (question,
            answer)
