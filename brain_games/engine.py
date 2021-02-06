import prompt


def welcome_user():
    """Greet user and return input username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def start(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    for i in range(1, ROUNDS_COUNT + 1):
        question, answer = game.round_generating()
        print('Question: ' + str(question))
        user_answer = input('Your answer: ')
        if user_answer.lower() == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            break
        if i == ROUNDS_COUNT:
            print('Congratulations, {}!'.format(name))


ROUNDS_COUNT = 3
