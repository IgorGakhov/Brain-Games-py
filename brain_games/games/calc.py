import prompt
from random import randint, choice

from brain_games.cli import welcome_user
from brain_games.engine.game_engine import generate_game_round

GAME_RULES_CALC = 'What is the result of the expression?'

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100

OPERATION_PLUS = '+'
OPERATION_MINUS = '-'
OPERATION_MULTIPLY = '*'

ARITHMETIC_OPERATIONS = [OPERATION_MINUS, OPERATION_PLUS, OPERATION_MULTIPLY]


def generate_game_data():
    # Генерируем данные и задаем вопрос пользователю
    random_number1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operation = choice(ARITHMETIC_OPERATIONS)
    computer_question = 'Question: {} {} {}'.format(random_number1,
                                                    operation, random_number2)
    print(computer_question)
    user_answer = prompt.integer('Your answer: ')

    value_set = [random_number1, random_number2, operation]

    return value_set, user_answer


def answer_is_correct(value_set, user_answer):
    # Определяем правильный ответ

    random_number1, random_number2, operation = value_set

    if operation == OPERATION_PLUS:
        target_result = random_number1 + random_number2
    elif operation == OPERATION_MINUS:
        target_result = random_number1 - random_number2
    elif operation == OPERATION_MULTIPLY:
        target_result = random_number1 * random_number2

    bool_result = target_result == user_answer

    return bool_result, target_result


def run_game():
    name = welcome_user()
    print(GAME_RULES_CALC)
    generate_game_round(name, generate_game_data, answer_is_correct)


if __name__ == '__main__':
    run_game()
