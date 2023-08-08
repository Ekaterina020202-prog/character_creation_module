from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str = None) -> str:
    """
    Симулирует действие атаки в зависимости от класса персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str, опционально): Класс персонажа (warrior, mage, healer).

    Returns:
        str: Сообщение, описывающее действие атаки.
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(3, 5)} очкам урона.')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(5, 10)} очкам урона.')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, '
                f'равный {5 + randint(-3, -1)} очкам урона.')


def defence(char_name: str, char_class: str = None) -> str:
    """
    Симулирует действие защиты в зависимости от класса персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str, опционально): Класс персонажа (warrior, mage, healer).

    Returns:
        str: Сообщение, описывающее действие защиты.
    """
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} очков урона.'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} очков урона.'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} очков урона.'


def special(char_name: str, char_class: str = None) -> str:
    """
    Симулирует действие защиты в зависимости от класса персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str, опционально): Класс персонажа (warrior, mage, healer).

    Returns:
        str: Сообщение, описывающее использование специальной способности.
    """
    if char_class == 'warrior':
        return f'{char_name} применил спец умение "Выносливость {80 + 25}"'
    if char_class == 'mage':
        return f'{char_name} применил спец умение "Атака {5 + 40}"'
    if char_class == 'healer':
        return f'{char_name} применил спец умение "Защита {10 + 30}"'


def start_training(char_name: str, char_class: str = None) -> str:
    """
    Начинает сессию тренировок для персонажа.

    Args:
        char_name (str): Имя персонажа.
        char_class (str, опционально): Класс персонажа (warrior, mage, healer).

    Returns:
        str: Сообщение, указывающее на окончание сессии тренировок.
    """
    if char_class == 'warrior':
        class_description = 'Воитель — могучий боец в ближнем бою.'
    if char_class == 'mage':
        class_description = 'Маг — искусный владыка стихийной магии.'
    if char_class == 'healer':
        class_description = 'Лекарь — сильный исцелитель ран.'

    print(f'Добро пожаловать, {char_name}!')
    print(f'Вы выбрали путь {class_description}')
    print('Тренируйтесь, чтобы овладеть своими навыками.')
    print('Введите одну из следующих команд: attack — для атаки, '
          'defence — для защиты от атаки или '
          'special — для использования специальной способности.')
    print('Если вы хотите пропустить тренировку, введите команду "skip".')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введите команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Сессия тренировок завершена.'


def choice_char_class() -> str:
    """
    Запрашивает у игрока выбор класса персонажа.

    Returns:
        str: Выбранный класс персонажа (warrior, mage, healer).
    """
    approve_choice = ''
    char_class = ''
    while approve_choice != 'y':
        char_class = input('Выберите класс персонажа: Воитель, Маг, Лекарь: ')
        if char_class == 'warrior':
            print('Воитель — бесстрашный боец в ближнем бою. '
                  'Сильный, выносливый и смелый.')
        if char_class == 'mage':
            print('Маг — умелый волшебник издалека. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный целитель. '
                  'Извлекает силу из природы, веры и духов.')
        approve_choice = input('Нажмите (Y), чтобы подтвердить выбор, '
                               'или любую другую клавишу, '
                               'чтобы выбрать другой класс: ').lower()
    return char_class
if __name__ == '__main__':
    run_screensaver()