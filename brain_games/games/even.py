from random import randint

from brain_games.engine.game_engine import run_game

GAME_RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(random_number):

    return True if random_number % 2 == 0 else False


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = '{}'.format(random_number)

    # Определяем правильный ответ
    if is_even(random_number):
        target_result = 'yes'
    else:
        target_result = 'no'

    return computer_question, target_result


def even_game():
    run_game(GAME_RULES_EVEN, generate_game_data)
