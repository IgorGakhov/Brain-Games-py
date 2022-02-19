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


def generate_game_round(name, generate_game_data, answer_is_correct):
    # Формируем логику игры и генерируем цикл раундов
    user_answer = True
    game_round = 1
    while user_answer is True and game_round <= GAME_ATTEMPTS:
        random_number, user_answer = generate_game_data()

        # Определяем правильный ответ
        bool_result, target_result = answer_is_correct(random_number,
                                                       user_answer)

        # Узнаем правильность ответа
        # и в зависимости от нее вызываем функцию
        if bool_result is True:
            user_answer = true_answer(game_round, name)
        else:
            user_answer = false_answer(user_answer, target_result, name)

        game_round += 1
