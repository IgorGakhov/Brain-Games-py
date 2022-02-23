from random import randint

from brain_games.engine.game_engine import run_game

GAME_RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_game_data = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = '{}'.format(str(random_game_data))

    return random_game_data, computer_question


def is_even(random_number):

    return True if random_number % 2 == 0 else False


def answer_is_correct(random_game_data, user_answer):
    # Определяем правильный ответ

    random_number = random_game_data

    if is_even(random_number) is True:
        target_result = 'yes'
        if user_answer == 'yes':
            bool_result = True
        else:
            bool_result = False

    if is_even(random_number) is False:
        target_result = 'no'
        if user_answer == 'no':
            bool_result = True
        else:
            bool_result = False

    return bool_result, target_result


def even_game():
    run_game(GAME_RULES_EVEN, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    even_game()
