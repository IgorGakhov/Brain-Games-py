from random import randint

from brain_games.engine.game_engine import generate_game_round

GAME_RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_game_data = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = 'Question: {}'.format(str(random_game_data))

    return random_game_data, computer_question


def answer_is_correct(random_game_data, user_answer):
    # Определяем правильный ответ

    random_number = random_game_data

    if random_number % 2 == 0:
        target_result = 'yes'
        if user_answer == 'yes':
            bool_result = True
        else:
            bool_result = False

    if random_number % 2 != 0:
        target_result = 'no'
        if user_answer == 'no':
            bool_result = True
        else:
            bool_result = False

    return bool_result, target_result


def run_game():
    generate_game_round(GAME_RULES_EVEN, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    run_game()
