from random import randint, choice
from typing import Callable

from brain_games.engine.game_engine import run_game

GAME_RULES_CALC = 'What is the result of the expression?'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

OPERATION_PLUS = '+'
OPERATION_MINUS = '-'
OPERATION_MULTIPLY = '*'

ARITHMETIC_OPERATIONS = (OPERATION_MINUS, OPERATION_PLUS, OPERATION_MULTIPLY)


def generate_game_data() -> tuple:
    # Генерируем данные и задаем вопрос пользователю
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operation = choice(ARITHMETIC_OPERATIONS)
    computer_question = f'{random_number1} {operation} {random_number2}'

    # Определяем правильный ответ
    target_result = False  # Дефолтное значение
    if operation == OPERATION_PLUS:
        target_result = random_number1 + random_number2
    elif operation == OPERATION_MINUS:
        target_result = random_number1 - random_number2
    elif operation == OPERATION_MULTIPLY:
        target_result = random_number1 * random_number2

    return computer_question, target_result


def calc_game() -> Callable:
    run_game(GAME_RULES_CALC, generate_game_data)
