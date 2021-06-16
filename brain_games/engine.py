import prompt

ROUNDS_COUNT = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.DESCRIPTION)
    for i in range(ROUNDS_COUNT):
        question, answer = game.generate_round()
        print('Question: ' + question)
        user_answer = input('Your answer: ')
        if user_answer.lower() == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
