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

    return True


def false_answer(user_answer, target_result, name):
    # Исполняется, если последний введенный ответ - неправильный
    print(FALSE_ANSWER.format(str(user_answer), str(target_result), name))

    return False


def run_game(game_rules, generate_game_data, answer_is_correct):
    # Приветствуем пользователя и выводим правила игры
    name = welcome_user()
    print(game_rules)

    # Формируем логику игры и генерируем цикл раундов
    user_answer = True
    game_round = 1
    while user_answer is True and game_round <= GAME_ATTEMPTS:
        random_game_value, computer_question = generate_game_data()
        print('Question: {}'.format(computer_question))
        user_answer = prompt.string('Your answer: ')

        # Определяем правильный ответ
        bool_result, target_result = answer_is_correct(random_game_value,
                                                       user_answer)

        # Узнаем правильность ответа
        # и в зависимости от нее вызываем функцию
        if bool_result is True:
            user_answer = true_answer(game_round, name)
        else:
            user_answer = false_answer(user_answer, target_result, name)

        game_round += 1
