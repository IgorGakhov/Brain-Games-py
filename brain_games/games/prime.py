from random import randint

from brain_games.engine.game_engine import run_game

GAME_RULES_PRM = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_game_data = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = 'Question: {}'.format(str(random_game_data))

    return random_game_data, computer_question


def is_prime(random_number):

    if random_number > 1:
        for i in range(2, int(random_number / 2) + 1):
            if (random_number % i) == 0:
                target_result = 'no'
                break
        else:
            target_result = 'yes'

    else:
        target_result = 'no'

    return target_result


def answer_is_correct(random_game_data, user_answer):
    # Определяем правильный ответ

    random_number = random_game_data

    target_result = is_prime(random_number)

    bool_result = target_result == user_answer

    return bool_result, target_result


def prime_game():
    run_game(GAME_RULES_PRM, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    prime_game()
