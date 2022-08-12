from typing import NoReturn

import prompt

GAME_ATTEMPTS = 3
WELCOME_MESSAGE = 'Welcome to the Brain Games!'
HELLO_MESSAGE = 'Hello, {}!'
ASK_NAME_MESSAGE = 'May I have your name? '
TRUE_ANSWER = 'Correct!'
FALSE_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, {}!'''
VICTORY_GAME_MESSAGE = 'Congratulations, {}!'


def run_game(game_rules: str, generate_game_data: tuple) -> NoReturn:
    # Приветствуем пользователя
    print(WELCOME_MESSAGE)
    name = prompt.string(ASK_NAME_MESSAGE)
    print(HELLO_MESSAGE.format(name))

    # Выводим правила игры, формируем логику игры и генерируем цикл раундов
    print(game_rules)
    game_round = 1

    while game_round <= GAME_ATTEMPTS:
        computer_question, target_result = generate_game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')

        # Узнаем правильность ответа
        bool_result = str(target_result) == user_answer.lower()

        # ... и в зависимости от выбора ответа вызываем функцию
        if not bool_result:
            # Исполняется, если последний введенный ответ - неправильный
            print(FALSE_ANSWER.format(user_answer, target_result, name))
            break

        # Исполняется, если последний введенный ответ - правильный
        print(TRUE_ANSWER)
        if game_round == GAME_ATTEMPTS:
            print(VICTORY_GAME_MESSAGE.format(name))

        game_round += 1
