from random import randint

from graphic_arts.graphic_arts.start_game_banner import run_screensaver
<<<<<<< HEAD


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс урон противнику равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
=======


def attack(char_name: str, char_class: str) -> str:
    """Дополнительная функция, вызывается при выборе действия персонажа.
    Выбор атаковать противника.
    Печатает результат применения.
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5,10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} не нанёс урон противнику')


def defence(char_name: str, char_class: str) -> str:
    """Дополнительная функция, вызывается при выборе действия персонажа.
    Выбор блокировать атаку противника.
    Печатает результат применения.
    """
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не блокировал урона')


def special(char_name: str, char_class: str) -> str:
    """Дополнительная функция, вызывается при выборе действия персонажа.
    Выбор: использовать суперсилу.
    Печатает результат применения.
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость '
                f'{80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Функция печатает в чем хорош твой персонаж.
    Предлагает пройти тренировку либо пропустить её.
    После выбора действия вызывается доп функцию действия.
    После повторяет запрос выбора действия.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
>>>>>>> 4da13291a55083fe69837b5dfeb476bf6815772e
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    commands = {'attack': character.attack,
                'defence': character.defence,
                'special': character.special
                }
    cmd = input('Введи команду: ')

    while cmd != 'skip':
        if cmd in commands:
            return print(commands[cmd])
    return print('Тренировка окончена.')


<<<<<<< HEAD
def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

=======
def choice_char_class() -> str:
    """Функция печатает на выбор трёх персонажей и выдает описание выбранного.
    Просит подтвердить выбор либо выбрать другогоперсонажа снова.
    Функция возбращает выбранного персонажа для дальнейших действий программы.
    """
>>>>>>> 4da13291a55083fe69837b5dfeb476bf6815772e
    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)

        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


<<<<<<< HEAD
def main() -> None:
    if __name__ == '__main__':
        run_screensaver()
        print('Приветствую тебя, искатель приключений!')
        print('Прежде чем начать игру...')
        char_name: str = input('...назови себя: ')
        print(f'Здравствуй, {char_name}! '
              'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
        print('Ты можешь выбрать один из трёх путей силы:')
        print('Воитель, Маг, Лекарь')
        char_class = choice_char_class(char_name)
        print(start_training(char_class))


main()
=======
if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
>>>>>>> 4da13291a55083fe69837b5dfeb476bf6815772e
