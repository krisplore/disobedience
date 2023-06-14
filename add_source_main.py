import gettext  # использую для перевода строк, обращенных к пользователю/администратору
import getopt  # использую функции модуля для обработки аргументов командной строки
import os
import sys  # понадобится для обработки ошибок в разборе аргументов командной строки
import yaml  # использую для записи словаря source в YAML файл
from add_source_functions import get_time, extract_tags, generate_id, generate_invite, set_type

EXTENSION = '.yaml'
_ = None


def main(argv):
    global _
    oslocale = os.getenv('LANG')
    language = gettext.translation("pet_project", localedir='locales', languages=[oslocale])
    language.install()
    _ = language.gettext
    print(oslocale)

    callsign = ''
    tags = ''
    invited_by = ''

    option_map = {    # словарь для связи опций командной строки с именами переменных словаря
        '-c': 'Callsign',
        '--callsign': 'Callsign',
        '-t': 'Tags',
        '--tags': 'Tags',
        '-i': 'Invited_by',
        '--invited_by': 'Invited_by'
    }

    # ключевое слово начинает блок кода, в котором обрабатываются ошибки
    # opts, args - кортеж, в котором будут храниться опции и аргументы, которые возвращаются функцией get opt
    # функция getopt.getopt() обрабатывает аргументы командной строки. Принимает 3 аргумента из списка аргументов arg
    # except - возникает только если вышло исключение при обработке аргументов
    # sys.exit(2) прерывает выполнение программы и выходит из нее с кодом 2
    try:
        opts, args = getopt.getopt(argv, 'c:t:i:', ['callsign=', 'tags=', 'invited_by='])  # теги не обязательны
    except getopt.GetoptError:  # срабатывает если пользователь хочет ввести неправильную опцию или пустой аргумент
        print(_('Invalid options or missing required arguments'))
        sys.exit(2)  # код возврата 2 - некорректный аргумент командной строки

    if '-c' not in [opt for opt, _ in opts] or '-i' not in [opt for opt, _ in opts]:
        print(_('Not all required arguments entered'))
        sys.exit(2)

    # создаю объект и инициализирую его с помощью класса gettext, представляет нулевой перевод (не выполняет действий)

    creation_time_str = get_time()
    modification_time_str = creation_time_str
    id_value = generate_id()

    source = {
        _('Callsign'): callsign,
        _('Tags'): tags,
        _('Invited_by'): invited_by,
        _('Id'): id_value,
        _('Type'): set_type(),
        _('Reliability'): 4.98,
        _('Note'): 'some new note',
        _('Created'): creation_time_str,
        _('Modified'): modification_time_str,
        _('Invite'): generate_invite(),
        _('Stats'): {
            _('Total_facts'): 0,
            _('Confirmed_facts'): 0,
            _('Refuted_facts'): 0
        }
    }

    for opt, arg in opts:
        dictionary_key = option_map.get(opt)
        if dictionary_key:
            source[dictionary_key] = arg

    source['Tags'] = extract_tags(tags)

    for key, value in source.items():
        print(key + ":", value)

    filename = 'data/source/' + id_value + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)


if __name__ == "__main__":
    main(sys.argv[1:])