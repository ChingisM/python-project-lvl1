import random


def numbers_generating():
    """Return two random generated numbers."""
    num1 = random.randint(11, 20)
    num2 = random.randint(1, 10)
    return [num1,
            num2]


def arithmetic_operator_generating():
    """Return a random chosen arithmetic operator as a string."""
    operator = random.choice(['+', '-', '*'])
    return operator


def question_generating(num1, num2, operator):
    """Return a formed question for the brain-game engine."""
    question = str(num1) + ' ' + operator + ' ' + str(num2)
    return question


def calculation_result(num1, num2, operator):
    """Return a result of an arithmetic operation with two numbers."""
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return str(result)


def round_generating():
    """Return generated question and answer for a round
    in the brain-game engine."""
    num1, num2 = numbers_generating()
    operator = arithmetic_operator_generating()
    question = question_generating(num1, num2, operator)
    answer = calculation_result(num1, num2, operator)
    return [question,
            answer]


# Description for the brain-game engine.
DESCRIPTION = 'What is the result of the expression?'
