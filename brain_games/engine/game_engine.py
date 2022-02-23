import prompt
from brain_games.cli import welcome_user

GAME_ATTEMPTS = 3
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


def true_answer(game_round, name):
    # Исполняется, если последний введенный ответ - правильный
    print(TRUE_ANSWER)
    if game_round == GAME_ATTEMPTS:
        print(VICTORY_GAME_MESSAGE.format(name))


def false_answer(user_answer, target_result, name):
    # Исполняется, если последний введенный ответ - неправильный
    print(FALSE_ANSWER.format(user_answer, target_result, name))


def run_game(game_rules, generate_game_data):
    # Приветствуем пользователя и выводим правила игры
    name = welcome_user()
    print(game_rules)

    # Формируем логику игры и генерируем цикл раундов
    game_round = 1
    while game_round <= GAME_ATTEMPTS:
        computer_question, target_result = generate_game_data()
        print('Question: {}'.format(str(computer_question)))
        user_answer = prompt.string('Your answer: ')

        # Узнаем правильность ответа
        bool_result = str(target_result) == user_answer

        # и в зависимости от выбора ответа вызываем функцию
        if not bool_result:
            false_answer(user_answer, target_result, name)
            break

        true_answer(game_round, name)
        game_round += 1
