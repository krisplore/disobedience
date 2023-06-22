import datetime  # использую для получания текущего времени
import gettext  # использую для перевода строк, обращенных к пользователю/администратору
import getopt  # использую функции модуля для обработки аргументов командной строки
import os
import secrets  # использую для создания уникальных строчек-приглашений в функции generate_invite
import string  # использую для создания списка - алфавита, для создания уникальных строчек-приглашений
import sys  # понадобится для обработки ошибок в разборе аргументов командной строки
import uuid  # использую для создания id источника, чтобы обеспечить уникальность идентификатора
import random
import locale

import yaml  # использую для записи словаря source в YAML файл

EXTENSION = '.yaml'
AMOUNT_OF_INVITATIONS = 2
INVITATION_LENGTH = 6


#  разделяет строку по знаку запятой, создает список подстрок
#  удаляет яет начальные и конечные пробелы, а цикл for проходит по каждой подстроке и добавляет ее в список tags
def extract_tags(tags):  # если запятой нет, в список добавляется только один элемент - вся строка tags
    tags = [item.strip() for item in tags.split(',') if item.strip()]
    return tags


# функция генерирует уникальный идентификатор на основе случайных чисел
# функция str преобразует объект UUID в строку
# функция в целом возвращает строковое представление UUID04
def generate_id():
    return str(uuid.uuid4())


# в настоящем - возвращает 1 - соответствует описанию типа human
def set_type():
    return 1


# генерирует список приглашений, состоящий из случайно сгенерированных строк из 6 символов английского алфавита в
# верхнем регистре без спорных символов
# создается список символов англ.яз. + цифры - спорные символы
# внутри цикла генератор списка, чтобы создать случайную строку из списка символов установленной длины
# дальше строка добавляется в список invite, а он по итогу возвращается
def generate_invite():
    alphabet = string.ascii_uppercase + string.digits
    excluded_characters = 'IiOo01l'
    characters = [c for c in alphabet if c not in excluded_characters]
    invite = []
    for _ in range(AMOUNT_OF_INVITATIONS):
        invite.append(''.join((secrets.choice(characters) for _ in range(INVITATION_LENGTH))))
    return invite


# внутри функции вызывается метод now() - возвращает объект, представляющий текущее время
# в формате datetime.datetime на основе этого классе
# затем вызывается метод timestamp() - возвращает отметку времени в виде числа float (кол-во секунд с 1.01.70)
# функция int() преобразует отметку в целое число int
def get_time():
    return int(datetime.datetime.now().timestamp())


# функция была необходима для перевода строк моего словаря, потому что функции gettext не принимает в качестве
# аргумента тип данных dict
# функция gettext.translation создает объект, который будет использоваться для перевода текста на английский язык
# метод install устанавливает объект translation как текущий переводчик
# translation.gettext(string) - выполняется перевод текста на английский

# def translate_string(string):
#     translation = gettext.translation('pet_project', localedir='locales', languages=['en'])
#     translation.install()
#     return translation.gettext(string)


# обработка аргументов командной строки, создание словаря source
# вывод информации на экран и запись в данных в yaml файл
def main(argv):
    startTime = (datetime.datetime.now().timestamp())
    callsign = ''
    tags = ''
    invited_by = ''

    osLocale = os.getenv('LANG')

    option_map = {    # словарь для связи опций командной строки с именами переменных словаря
        '-c': 'callsign',
        '--callsign': 'callsign',
        '-t': 'tags',
        '--tags': 'tags',
        '-i': 'invited_by',
        '--invited_by': 'invited_by'
    }

    # создаю объект languages_en, который инициализируется с помощью модуля gettext
    # устанавливаю объект в качестве переводчика
    print (osLocale)
    language = gettext.translation('pet_project', localedir='locales', languages=[osLocale])
    language.install()

    _ = language.gettext  # присваиваю псевдоним для метода gettext чтобы сократить код

    # ключевое слово начинает блок кода, в котором обрабатываются ошибки
    # opts, args - кортеж, в котором будут храниться опции и аргументы, которые возвращаются функцией get opt
    # функция getopt.getopt() обрабатывает аргументы командной строки. Принимает 3 аргумента из списка аргументов arg
    # except - возникает только если вышло исключение при обработке аргументов
    # sys.exit(2) прерывает выполнение программы и выходит из нее с кодом 2
    try:
        opts, args = getopt.getopt(argv, 'c:t:i:', ['callsign=', 'tags=', 'invited_by='])  # теги не обязательны
    except getopt.GetoptError:  # срабатывает если пользователь хочет ввести неправильную опцию или пустой аргумент
        print(_('There is something wrong with arguments'))
        sys.exit(2)  # код возврата 2 - некорректный аргумент командной строки

    if '-c' not in [opt for opt, _ in opts] or '-t' not in [opt for opt, _ in opts] or '-i' not in [opt for opt, _ in opts]:
        print(gettext.gettext('There is something wrong with arguments'))
        sys.exit(2)

    gettext.gettext(_('oi fuckface'))

    # создаю объект и инициализирую его с помощью класса gettext, представляет нулевой перевод (не выполняет действий)

    en_translations = gettext.NullTranslations()
    en_translations.install()  #

    creation_time_str = get_time()
    modification_time_str = creation_time_str

    source = {
        'callsign': callsign,
        'tags': extract_tags(tags),
        'invited_by': invited_by,
        'id': generate_id(),
        'type': set_type(),
        'reliability': 4.98,
        'note': 'some new note',
        'created': creation_time_str,
        'modified': modification_time_str,
        'invite': generate_invite(),
        'stats': {
            'total_facts': 0,
            'confirmed_facts': 0,
            'refuted_facts': 0
        }
    }

    for opt, arg in opts:
        dictionary_key = option_map.get(opt)
        if dictionary_key:
            source[dictionary_key] = arg

    for key, value in source.items():  # перебираю ключи и значения словаря
        print(f'{key}: {value}')  # вывожу их на экран

    filename = 'data/source/' + source['id'] + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)

    endTime = (datetime.datetime.now().timestamp())
    elapsed = endTime - startTime
    print('Time is ', elapsed*1000)

if __name__ == "__main__":
    main(sys.argv[1:])
