import prompt
from random import randint

from brain_games.cli import welcome_user

GAME_RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_ATTEMPTS = 3
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER_YES = '''\'yes\' is wrong answer ;(. Correct answer was \'no\'.
Let\'s try again, {}!'''
FALSE_ANSWER_NO = '''\'no\' is wrong answer ;(. Correct answer was \'yes\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


def answer_is_correct(random_number, user_answer):
    # Определяем, четное ли число
    even = random_number % 2 == 0

    # Определяем правильный ответ

    # Исход события - True, ответ - True
    # Исход события - False, ответ - True
    if (even and user_answer == 'yes') or (not even and user_answer == 'no'):
        bool_result = True

    # Исход события - True, ответ - False
    # Исход события - False, ответ - False
    elif (even and user_answer != 'yes') or (not even and user_answer != 'no'):
        bool_result = False

    return bool_result, even


def true_answer(game_round, name):
    # Исполняется, если последний введенный ответ - правильный
    print(TRUE_ANSWER)
    if game_round == GAME_ATTEMPTS:
        print(VICTORY_GAME_MESSAGE.format(name))

    return True


def false_answer(name, even):
    # Исполняется, если последний введенный ответ - неправильный
    if even is True:
        print(FALSE_ANSWER_NO.format(name))
    else:
        print(FALSE_ANSWER_YES.format(name))

    return False


def generate_game_round(name):
    # Формируем логику игры и генерируем цикл раундов
    user_answer = True
    game_round = 1
    while user_answer is True and game_round <= GAME_ATTEMPTS:
        random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        computer_question = 'Question: {}'.format(str(random_number))
        print(computer_question)
        user_answer = prompt.string('Your answer: ')

        # Определяем правильный ответ
        bool_result, even = answer_is_correct(random_number, user_answer)

        # Узнаем правильность ответа
        # и в зависимости от нее вызываем функцию
        if bool_result is True:
            user_answer = true_answer(game_round, name)
        else:
            user_answer = false_answer(name, even)

        game_round += 1


def run_game():
    name = welcome_user()
    print(GAME_RULES_EVEN)
    generate_game_round(name)


if __name__ == '__main__':
    run_game()
