import random

# Description for the brain-game engine.
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, diff, length):
    """Return a generated arithmetic progression."""
    progression = [start]
    new_element = start
    for i in range(1, length):
        new_element += diff
        progression.append(new_element)
    return progression


def generate_round():
    """Return generated question and answer for a round
    in the brain-game engine."""
    start, diff, length = random.randint(1, 25), random.randint(2, 9), random.choice([5, 6, 7, 8, 9, 10])
    progression = generate_progression(start, diff, length)
    index_of_element = random.randint(0, length - 1)
    required_element = progression[index_of_element]
    answer = str(required_element)
    progression[index_of_element] = '..'
    question = ''
    for i in range(0, length):
        question = question + str(progression[i]) + ' '
    return (question,
            answer)
