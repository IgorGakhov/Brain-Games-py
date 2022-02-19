import math
import prompt
from random import randint

from brain_games.cli import welcome_user
from brain_games.engine.game_engine import generate_game_round

GAME_RULES_GCD = 'Find the greatest common divisor of given numbers.'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = '{} {}'.format(random_number1, random_number2)
    print('Question: {}'.format(str(computer_question)))
    user_answer = prompt.integer('Your answer: ')

    value_set = [random_number1, random_number2]

    return value_set, user_answer


def answer_is_correct(value_set, user_answer):
    # Определяем правильный ответ

    random_number1, random_number2 = value_set

    target_result = math.gcd(random_number1, random_number2)
    bool_result = target_result == user_answer

    return bool_result, target_result


def run_game():
    name = welcome_user()
    print(GAME_RULES_GCD)
    generate_game_round(name, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    run_game()
