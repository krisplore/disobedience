import gettext  # использую для перевода строк, обращенных к пользователю/администратору
import getopt  # использую функции модуля для обработки аргументов командной строки
import os
import sys  # понадобится для обработки ошибок в разборе аргументов командной строки
import yaml  # использую для записи словаря source в YAML файл
from add_source_functions import get_time, extract_tags, generate_id, generate_invite, set_type

EXTENSION = '.yaml'


def main(argv):
    callsign = ''
    tags = ''
    invited_by = ''

    oslocale = os.getenv('LANG')

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
    print(oslocale)
    language = gettext.translation('pet_project', localedir='locales', languages=[oslocale])
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
        print(_('There is something wrong with all arguments'))
        sys.exit(2)  # код возврата 2 - некорректный аргумент командной строки

    if '-c' not in [opt for opt, _ in opts] or '-i' not in [opt for opt, _ in opts]:
        print(gettext.gettext('There is something wrong with arguments'))
        sys.exit(2)

    gettext.gettext(_('oi blackface'))

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
    keys_to_print = ['callsign', 'id', 'invited_by', 'invite', 'created']

    for key in keys_to_print:
        print(f"{_(key)}: {source[key]}")

    # for opt, arg in opts:
    #     dictionary_key = option_map.get(opt)
    #     if dictionary_key:
    #         source[dictionary_key] = arg

    for key, value in source.items():  # перебираю ключи и значения словаря
        print(_(key))  # вывожу их на экран
        print(f'{value}')

    filename = 'data/source/' + source['id'] + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)


if __name__ == "__main__":
    main(sys.argv[1:])