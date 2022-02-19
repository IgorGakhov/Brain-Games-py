import prompt
from random import randint

from brain_games.cli import welcome_user

GAME_RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GAME_ATTEMPTS = 3
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER_CALC_RESULT = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


def answer_is_correct(random_number, user_answer):
    # Определяем правильный ответ
    if random_number > 1:
        for i in range(2, int(random_number / 2) + 1):
            if (random_number % i) == 0:
                math_result = 'no'
                break
        else:
            math_result = 'yes'

    else:
        math_result = 'no'

    result_is_True = math_result == user_answer

    return result_is_True, math_result


def true_answer(game_round, name):
    # Исполняется, если последний введенный ответ - правильный
    print(TRUE_ANSWER)
    if game_round == GAME_ATTEMPTS:
        print(VICTORY_GAME_MESSAGE.format(name))

    return True


def false_answer(user_answer, math_result, name):
    # Исполняется, если последний введенный ответ - неправильный
    print(FALSE_ANSWER_CALC_RESULT.format(str(user_answer), str(math_result), name))

    return False


def generate_game_round(name):
    # Формируем логику игры и генерируем цикл раундов
    user_answer = True
    game_round = 1
    while user_answer is True and game_round <= GAME_ATTEMPTS:
        random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        computer_question = '{}'.format(random_number)
        print('Question: {}'.format(str(computer_question)))
        user_answer = prompt.string('Your answer: ')

        # Определяем правильный ответ
        bool_answer_result, math_result = answer_is_correct(random_number, user_answer)

        # Узнаем правильность ответа
        # и в зависимости от нее вызываем функцию
        if bool_answer_result is True:
            user_answer = true_answer(game_round, name)
        else:
            user_answer = false_answer(user_answer, math_result, name)

        game_round += 1


def run_game():
    name = welcome_user()
    print(GAME_RULES_PRIME)
    generate_game_round(name)


if __name__ == '__main__':
    run_game()