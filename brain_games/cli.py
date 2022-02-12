import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    welcome_message = 'Hello, {}!'.format(name)
    print(welcome_message)
    return name

#welcome_user()