import prompt
from random import randint

from brain_games.cli import welcome_user

GAME_RULES_PGS = 'What number is missing in the progression?'
GAME_ATTEMPTS = 3
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER_CALC_RESULT = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'

PROGRESSION_START_VALUE_MIN = 1
PROGRESSION_START_VALUE_MAX = 50

PROGRESSION_STEP_VALUE_MIN = -20
PROGRESSION_STEP_VALUE_MAX = 20

PROGRESSION_LENGTH_VALUE_MIN = 5
PROGRESSION_LENGTH_VALUE_MAX = 10


def generate_progression():
    start_value = randint(PROGRESSION_START_VALUE_MIN, PROGRESSION_START_VALUE_MAX)
    length_value = randint(PROGRESSION_LENGTH_VALUE_MIN, PROGRESSION_LENGTH_VALUE_MAX)
    step_value = randint(PROGRESSION_STEP_VALUE_MIN, PROGRESSION_STEP_VALUE_MAX)

    progression = []
    for i in range(start_value, start_value + (length_value * step_value), step_value):
        progression.append(str(i))

    index_skip_value = randint(0, length_value - 1)
    skip_value = progression[index_skip_value]
    progression[index_skip_value] = '..'
    progression = ' '.join(progression)

    return progression, skip_value


def answer_is_correct(skip_value, user_answer):
    # Определяем правильный ответ
    result_is_True = int(skip_value) == user_answer

    return result_is_True


def true_answer(game_round, name):
    # Исполняется, если последний введенный ответ - правильный
    print(TRUE_ANSWER)
    if game_round == GAME_ATTEMPTS:
        print(VICTORY_GAME_MESSAGE.format(name))

    return True


def false_answer(user_answer, skip_value, name):
    # Исполняется, если последний введенный ответ - неправильный
    print(FALSE_ANSWER_CALC_RESULT.format(str(user_answer), str(skip_value), name))

    return False


def generate_game_round(name):
    # Формируем логику игры и генерируем цикл раундов
    user_answer = True
    game_round = 1
    while user_answer is True and game_round <= GAME_ATTEMPTS:
        progression, skip_value = generate_progression()
        computer_question = '{}'.format(progression)
        print('Question: {}'.format(str(computer_question)))
        user_answer = prompt.integer('Your answer: ')

        # Определяем правильный ответ
        bool_answer_result = answer_is_correct(skip_value, user_answer)

        # Узнаем правильность ответа
        # и в зависимости от нее вызываем функцию
        if bool_answer_result is True:
            user_answer = true_answer(game_round, name)
        else:
            user_answer = false_answer(user_answer, skip_value, name)

        game_round += 1


def run_game():
    name = welcome_user()
    print(GAME_RULES_PGS)
    generate_game_round(name)


if __name__ == '__main__':
    run_game()
