from random import randint
from typing import Callable

from brain_games.engine.game_engine import run_game

GAME_RULES_PRG = 'What number is missing in the progression?'

PROGRESSION_START_VALUE_MIN = 1
PROGRESSION_START_VALUE_MAX = 50

PROGRESSION_STEP_VALUE_MIN = 3
PROGRESSION_STEP_VALUE_MAX = 30

PROGRESSION_LENGTH_VALUE_MIN = 5
PROGRESSION_LENGTH_VALUE_MAX = 10


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    start_value = randint(
        PROGRESSION_START_VALUE_MIN, PROGRESSION_START_VALUE_MAX
    )
    length_value = randint(
        PROGRESSION_LENGTH_VALUE_MIN, PROGRESSION_LENGTH_VALUE_MAX
    )

    # Чтобы последовательность могла быть убывающей,
    # возведем в степень (-1) от 1 до 2 раз в step_value_sign
    # Это избавит нас от вероятности нулевого шага при randint(-n, n)
    step_value_sign = (-1) ** randint(1, 2)
    step_value = step_value_sign * randint(
        PROGRESSION_STEP_VALUE_MIN, PROGRESSION_STEP_VALUE_MAX
    )

    progression = []
    progression_max_value = start_value + (length_value * step_value)
    for i in range(start_value, progression_max_value, step_value):
        progression.append(str(i))

    # Определяем отбрасываемое число и заменяем его двумя точками
    index_skip_value = randint(0, length_value - 1)
    target_result = progression[index_skip_value]
    progression[index_skip_value] = '..'
    progression = ' '.join(progression)

    computer_question = f'{progression}'

    return computer_question, target_result


def progression_game() -> Callable:
    run_game(GAME_RULES_PRG, generate_game_data)
