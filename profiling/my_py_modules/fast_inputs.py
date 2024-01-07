"""Написанные мной (Даниилом Звягиным ИУ7-13Б)
модули для быстрого ввода разных типов данных
с разными проверками
"""
from typing import Literal, Optional, Union, List
from random import randint
import re
import os.path


def param_input(data_type: Optional[Union[int, float, str]],
                params: str = '.*', custom_prompt: Optional[str] = '') -> Union[int, str, float]:
    """Осуществляет ввод переменной указанного типа
    с указанными параметрами и т.д., осущетвляет все проверки
    и просит ввод заново в случае ошибок

    :param data_type: Тип данных
    :type data_type: Optional[Union[int, float, str]]
    :param params: Параметры переменной  для числовых значений
    вида 'n<0' или 'n!=2'. В качестве имени переменной
    использовать только 'n'. Для строк принимает regex, defaults to '.*'
    :type params: str, optional
    :param custom_promt: Приглашение ко вводу
    :type custom_promt: str, optional 
    :return: Возвращает введённую переменную
    :rtype: Union[int, str, float]
    """

    # Проверка на неправильный тип данных
    if data_type not in [int, str, float]:
        print(
            "Функции ввода переменной был предоставлен неправильный тип данных: ",
            data_type, "\nОжидалось int | float | str."
        )
        raise ValueError()

    if data_type == str:
        try:
            pattern = re.compile(params)
        except re.error:
            print("Ошибка в регулярном выражении для ввода строки")
            raise ValueError

        if params == r"^((.+)\/)?([^\/]+)$":
            error_prompt = "Введите действительное имя файла"
        else:
            error_prompt = "Введите строку" +\
                f" (паттерна вида {params})" if params != '.*' else ''
        error_prompt += ': '

        prompt = custom_prompt if custom_prompt else error_prompt

        input_string = input(prompt)
        while not re.fullmatch(pattern, input_string):
            input_string = input(error_prompt)

        return input_string

    special_check_flag = params != '.*'

    if special_check_flag:
        if re.search(r'[^n<=>0-9\-\+\/\*\.]', params) or params.count('n') != 1:
            print("Проверка параметров для ввода числа нашла ошибку в паттерне")
            raise ValueError

    n = None

    error_prompt = "Введите число (типа "
    error_prompt += "int" if data_type == int else "float"
    error_prompt += f" вида {params}" if special_check_flag else ''
    error_prompt += f"): "

    prompt = custom_prompt if custom_prompt else error_prompt

    while type(n) is not data_type or special_check_flag and not eval(params.replace('n', str(n))):
        try:
            n = data_type(input(prompt))
            if special_check_flag and not eval(params.replace('n', str(n))):
                print(error_prompt)

        except ValueError:
            print(error_prompt)
            n = None
            continue

    return n


def input_list(n: int,
               data_type: Optional[Union[int, float, str]] = float,
               input_style: Optional[Literal["lab", "normal"]] = 'lab'
               ) -> List:
    """Осуществляет ввод списка с длиной n

    :param n: Длина списка
    :type n: int > 0
    :param data_type: Тип данных (поддерживается float, int, str), defaults to float
    :type data_type: Optional[Union[int, float, str]], optional
    :param input_style: Стиль ввода данных (lab - по одному значению в строке;
    normal - все элементы, разделённые робелами), defaults to 'lab'
    :type input_style: Optional[Literal[&quot;lab&quot;, &quot;normal&quot;]], optional
    :return: Возвращает введённый список с соответствующими параметрами
    :rtype: List
    """

    # Проверка размера списка
    if n < 1 or type(n) is not int:
        print("Функции ввода списка был передан неправильный размер массива")
        raise ValueError()

    # Проверка на неправильный тип данных
    if data_type not in [int, str, float]:
        print(
            "Функции ввода списка был предоставлен неправильный тип данных: ",
            data_type, "\nОжидалось int | float | str."
        )
        raise ValueError()

    # Проверка на неправильный стиль ввода
    if input_style not in ['lab', 'normal']:
        print(
            "Функции ввода списка был предоставлен неправильный стиль ввода: ",
            input_style, "\nОжидалось 'lab' | 'normal'"
        )
        raise ValueError()

    arr = [0]*n

    if input_style == 'lab':
        for i in range(n):
            arr[i] = param_input(
                data_type=data_type, custom_prompt=f"Введите {i+1}-й элемент списка: ")
    else:
        arr[i] = list(map(data_type, input("Введите список\n> ").split()))

    if len(arr) < n:
        print("Введено недостаточное количество элементов!")
        raise ValueError
    for _ in range(len(arr)-n):
        arr.pop()

    return arr


def input_matrix(m: int, n: Optional[int] = 0,
                 data_type: Optional[Union[int, float, str]] = float,
                 input_style: Optional[Literal["lab", "normal"]] = 'lab') -> List[List]:
    """Предлагает пользователю ввести матрицу с указанными параметрами,
    возвращает введённую матрицу

    :param m: размер m матрицы
    :type m: int > 0
    :param n: размер n матрицы, в случае отсутствия ввода копирует m, defaults to 0
    :type n: Optional[int > 0], optional
    :param data_type: тип данных для ввода, defaults to float
    :type data_type: Union[int, float, str], optional
    :param input_style: Стиль ввода (по строкам или по ячейкам), где lab - это
    по ячейкам, а normal - по строкам, defaults to 'lab'
    :type input_style: Literal["lab", "normal"], optional
    :return: Возвращает введённую матрицу с соответствующими параметрами
    :rtype: List[List]
    """

    # Если n не указан, создаём квадратную матрицу
    if n == 0:
        n = m

    if n < 1 or m < 1:
        print(
            "Функции ввода матрицы был предоставлен неправильниый размер"
        )
        raise ValueError()

    # Проверка на неправильный тип данных
    if data_type not in [int, str, float]:
        print(
            "Функции ввода матрицы был предоставлен неправильный тип данных: ",
            data_type, "\nОжидалось int | float | str."
        )
        raise ValueError()

    # Проверка на неправильный стиль ввода
    if input_style not in ['lab', 'normal']:
        print(
            "Функции ввода матрицы был предоставлен неправильный стиль ввода: ",
            input_style, "\nОжидалось 'lab' | 'normal'"
        )
        raise ValueError()

    matrix = [[0]*n for _ in range(m)]

    try:
        for i in range(m):
            if input_style == 'lab':
                for j in range(n):
                    matrix[i][j] = \
                        param_input(data_type=data_type,
                                    custom_prompt=f"Введите {j+1}-й элемент {i+1}-й строки матрицы: "
                                    )
            else:
                matrix[i] = list(map(data_type, input(
                    f"Введите {i+1}-ю строку матрицы\n> "
                ).split()))
    except ValueError:
        print(
            "Были введены данные неправильного типа, ожидался ",
            data_type, "\nсоболезную..."
        )
        return exit(1)

    return matrix


def rand_fill(arr: List, min_value: Optional[int] = -100,
              max_value: Optional[int] = 100) -> List:
    """Заполняет список случайными значениями по заданным параметрам

    :param arr: Список для заполнения
    :type arr: List
    :param min_value: Минимальное значение, defaults to -100
    :type min_value: Optional[int], optional
    :param max_value: Максимальное значение, defaults to 100
    :type max_value: Optional[int], optional
    :return: Список, заполненный случайными числами
    :rtype: List
    """
    if min_value >= max_value:
        print("Минимальное значение должно быть меньше, либо равно максимальному!")
        raise ValueError

    if not isinstance(min_value, int) or not isinstance(max_value, int):
        print("Минимальное и максимальное значения должны быть целочисленными")
        raise TypeError

    try:
        _ = (e for e in arr)
    except TypeError:
        print("Переданный в параметр списка объект не итерируемый!")
        raise TypeError

    for i in range(len(arr)):
        arr[i] = randint(min_value, max_value)

    return arr


def relative_to_absolute(path: str) -> str:
    """Обрабатывает все вхождения вида ../ или ./

    :param path: Путь к файлу
    :type path: str
    :return: Преобразованный путь
    :rtype: str
    """
    sep = os.path.sep
    args = path.split(sep)

    i = 0
    while i < len(args):

        if args[i] == '.':
            args.pop(i)

        if args[i] == '..':
            if i == 0:
                args.pop(i)
            else:
                args.pop(i)
                i -= 1
                args.pop(i)
                i -= 1

        # print(args)
        i += 1

    path = sep + os.path.join(*args)
    return path


def input_filename(mode: Optional[Literal[0, 1, 2]] = 1, current_path: Optional[str] = '', custom_prompt: Optional[str] = '') -> str:
    """Осуществляет ввод имени файла с 
    проверкой файла на существование

    :param mode: Режим работы: 1 - существующий файл, 0 - несуществующий файл, 
    2 - любой действительный путь к файлу (все папки должны существовать)
    :mode mode: Literal[1, 2, 3], optional
    :param custom_promt: Приглашение ко вводу
    :type custom_promt: str, optional 
    :param current_path: Путь к папке для относительных путей 
    :type curent_path: str, optional 
    :return: Имя файла, если оно было введено успешно
    :rtype: str
    """
    current_dir = '/'
    if current_path:
        if os.path.isdir(current_path):
            current_dir = current_path
        else:
            print(current_path)
            raise ValueError

    filename = None
    if not custom_prompt:
        custom_prompt = "Введите имя файла: "

    while True:
        filename = param_input(str, r"^((.+)\/)?([^\/]+)$", custom_prompt)
        if filename[0] not in "./" or filename[:2] != "./":
            filename = "./"+filename
        if filename[0] == '.' and filename[1] == '/':
            if filename[1] == '.':
                filename = os.path.join(current_dir, filename)
            else:
                filename = filename.replace('.', current_dir, 1)

        filename = relative_to_absolute(filename)
        # print(current_dir)
        # print(filename)
        if mode == 0:
            if not os.path.exists(filename):
                break
            else:
                print(f"Файл с таким именем и путём уже существует")
        elif mode == 1:
            if os.path.exists(filename):
                break
            else:
                print(f"Не найдено файла {filename}")
        else:
            if os.path.isdir(os.path.dirname(filename)):
                break
            else:
                print(
                    "Ошибка в пути к файлу. Вероятнее всего одной из папок не существует.")

    return filename
