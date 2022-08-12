import math
from random import randint
from typing import Callable

from brain_games.engine.game_engine import run_game

GAME_RULES_GCD = 'Find the greatest common divisor of given numbers.'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = f'{random_number1} {random_number2}'

    # Определяем правильный ответ
    target_result = math.gcd(random_number1, random_number2)

    return computer_question, target_result


def gcd_game() -> Callable:
    run_game(GAME_RULES_GCD, generate_game_data)
