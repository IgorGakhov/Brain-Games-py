import prompt
from brain_games.cli import welcome_user

GAME_ATTEMPTS = 3
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


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
        bool_result = str(target_result) == user_answer.lower()

        # ...и в зависимости от выбора ответа вызываем функцию
        if not bool_result:
            # Исполняется, если последний введенный ответ - неправильный
            print(FALSE_ANSWER.format(user_answer, target_result, name))
            break

        # Исполняется, если последний введенный ответ - правильный
        print(TRUE_ANSWER)
        if game_round == GAME_ATTEMPTS:
            print(VICTORY_GAME_MESSAGE.format(name))

        game_round += 1
