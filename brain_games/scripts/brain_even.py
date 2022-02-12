import prompt
from random import randint

from brain_games.cli import welcome_user

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_ATTEMPTS = 3
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER_YES = '\'yes\' is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, {}!'
FALSE_ANSWER_NO = '\'no\' is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again, {}!'
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


def even_game(name):

    print(GAME_RULES)

    answer = True
    game_round = 1
    while answer == True and game_round <= GAME_ATTEMPTS:
        random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        print('Question: {}'.format(str(random_number)))
        answer = prompt.string('Your answer: ')

        if random_number % 2 == 0 and answer == 'yes':      # Исход события - True, ответ - True
            answer = True
            print(TRUE_ANSWER)
            game_round += 1
            if game_round == GAME_ATTEMPTS + 1:
                print(VICTORY_GAME_MESSAGE.format(name))
        elif random_number % 2 != 0 and answer == 'no':     # Исход события - False, ответ - True
            answer = True
            print(TRUE_ANSWER)
            game_round += 1
            if game_round == GAME_ATTEMPTS + 1:
                print(VICTORY_GAME_MESSAGE.format(name))
        elif random_number % 2 == 0 and answer != 'yes':    # Исход события - True, ответ - False
            answer = False
            print(FALSE_ANSWER_NO.format(name))
            game_round += 1
        elif random_number % 2 != 0 and answer != 'no':     # Исход события - False, ответ - False
            answer = False
            print(FALSE_ANSWER_YES.format(name))
            game_round += 1


name = welcome_user()
even_game(name)
