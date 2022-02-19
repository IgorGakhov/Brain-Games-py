import prompt
from random import randint

from brain_games.cli import welcome_user
from brain_games.engine.game_engine import generate_game_round

GAME_RULES_PRM = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю

    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    computer_question = 'Question: {}'.format(str(random_number))
    print(computer_question)
    user_answer = prompt.string('Your answer: ')

    return random_number, user_answer


def answer_is_correct(random_number, user_answer):
    # Определяем правильный ответ
    if random_number > 1:
        for i in range(2, int(random_number / 2) + 1):
            if (random_number % i) == 0:
                target_result = 'no'
                break
        else:
            target_result = 'yes'

    else:
        target_result = 'no'

    bool_result = target_result == user_answer

    return bool_result, target_result


def run_game():
    name = welcome_user()
    print(GAME_RULES_PRM)
    generate_game_round(name, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    run_game()
