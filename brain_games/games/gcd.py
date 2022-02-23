import math
from random import randint

from brain_games.engine.game_engine import run_game

GAME_RULES_GCD = 'Find the greatest common divisor of given numbers.'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)

    random_game_data = [random_number1, random_number2]
    computer_question = '{} {}'.format(random_number1, random_number2)

    return random_game_data, computer_question


def answer_is_correct(random_game_data, user_answer):
    # Определяем правильный ответ

    random_number1, random_number2 = random_game_data

    target_result = math.gcd(random_number1, random_number2)
    bool_result = target_result == int(user_answer)

    return bool_result, target_result


def gcd_game():
    run_game(GAME_RULES_GCD, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    gcd_game()
