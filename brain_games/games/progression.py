import prompt
from random import randint

from brain_games.cli import welcome_user
from brain_games.engine.game_engine import generate_game_round

GAME_RULES_PROGRESSION = 'What number is missing in the progression?'

PROGRESSION_START_VALUE_MIN = 1
PROGRESSION_START_VALUE_MAX = 50

PROGRESSION_STEP_VALUE_MIN = -20
PROGRESSION_STEP_VALUE_MAX = 20

PROGRESSION_LENGTH_VALUE_MIN = 5
PROGRESSION_LENGTH_VALUE_MAX = 10


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    start_value = randint(PROGRESSION_START_VALUE_MIN,
                          PROGRESSION_START_VALUE_MAX)
    length_value = randint(PROGRESSION_LENGTH_VALUE_MIN,
                           PROGRESSION_LENGTH_VALUE_MAX)
    step_value = randint(PROGRESSION_STEP_VALUE_MIN,
                         PROGRESSION_STEP_VALUE_MAX)

    progression = []
    progression_max_value = start_value + (length_value * step_value)
    for i in range(start_value, progression_max_value, step_value):
        progression.append(str(i))

    index_skip_value = randint(0, length_value - 1)
    skip_value = int(progression[index_skip_value])
    progression[index_skip_value] = '..'
    progression = ' '.join(progression)

    computer_question = '{}'.format(progression)
    print('Question: {}'.format(str(computer_question)))
    user_answer = prompt.integer('Your answer: ')

    return skip_value, user_answer


def answer_is_correct(skip_value, user_answer):
    # Определяем правильный ответ
    target_result = skip_value
    bool_result = target_result == user_answer

    return bool_result, target_result


def run_game():
    name = welcome_user()
    print(GAME_RULES_PROGRESSION)
    generate_game_round(name, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    run_game()
