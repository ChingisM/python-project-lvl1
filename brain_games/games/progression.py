import random


def initial_data_generating():
    """Return three random generated numbers as an initial data
    for a "progression_generating" function."""
    start = random.randint(1, 25)
    diff = random.randint(2, 9)
    length = random.choice([5, 6, 7, 8, 9, 10])
    return [start,
            diff,
            length]


def progression_generating(start, diff, length):
    """Return a generated arithmetic progression."""
    progression = [start]
    new_element = start
    for i in range(1, length):
        new_element += diff
        progression.append(new_element)
    return progression


def required_element_generating(progression, length):
    """Return random generated an index and a value of progression's element."""
    index_of_element = random.randint(0, length - 1)
    required_element = progression[index_of_element]
    return [required_element,
            index_of_element]


def question_generating(progression, length, index_of_element):
    """Return a formed question for the brain-game engine."""
    progression[index_of_element] = '..'
    question = ''
    for i in range(0, length):
        question = question + str(progression[i]) + ' '
    return question


def round_generating():
    """Return generated question and answer for a round
    in the brain-game engine."""
    start, diff, length = initial_data_generating()
    progression = progression_generating(start, diff, length)
    required_element, index_of_element = \
        required_element_generating(progression, length)
    answer = str(required_element)
    question = question_generating(progression, length, index_of_element)
    return [question,
            answer]


# Description for the brain-game engine.
DESCRIPTION = 'What number is missing in the progression?'
