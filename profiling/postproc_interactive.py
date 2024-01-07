from random import randint
from my_py_modules import fast_inputs
import matplotlib.pyplot as plt
import os

DATA_DIR = "data"
PREPROC_DATA_DIR = "preproc_data"
POSTPROC_DATA_DIR = "postproc_data"

ADRESS_FILENAME_DICT = {
    1: "square_brackets_sort",
    2: "pure_pointer_sort",
    3: "sum_pointer_sort",
}

OPTIMIZATION_FILENAME_DICT = {1: "O0", 2: "O2"}

SORTED_FILENAME_DICT = {0: "ordered", 1: "random"}

GRAPH_MODE_NAME_DICT = {
    1: "simple",
    2: "error",
    3: "box",
}

MARKERS = ["D", "h", "+", "x", "*", "s", "1", "^", "."]
COLORS = ["r", "g", "b", "c", "m", "y"]


def sort_paired(src, pair):
    for i in range(len(src) - 1):
        for j in range(len(src) - 1 - i):
            if src[j] > src[j + 1]:
                src[j], src[j + 1] = src[j + 1], src[j]
                pair[j], pair[j + 1] = pair[j + 1], pair[j]


def sort_connected(src, a1, a2):
    for i in range(len(src) - 1):
        for j in range(len(src) - 1 - i):
            if src[j] > src[j + 1]:
                src[j], src[j + 1] = src[j + 1], src[j]
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
                a2[j], a2[j + 1] = a2[j + 1], a2[j]


def parse_avg(dstx, dsty, file):
    dstx.clear()
    dsty.clear()

    dataline = file.readline()
    while dataline != "":
        datapair = dataline.strip().split()
        dstx.append(float(datapair[0]))
        dsty.append(float(datapair[1]))
        dataline = file.readline()


def parse_to_dict(x_keys, y_dict, f):
    dataline = f.readline()

    while dataline != "":
        datapair = dataline.strip().split()
        key = float(datapair[0])
        if key not in x_keys:
            x_keys.append(key)

        value = int(datapair[1])

        if not key in y_dict:
            y_dict[key] = []
        y_dict[key].append(value)

        dataline = f.readline()


def parse_error(xdst, mindst, maxdst, file):
    xdst.clear()
    mindst.clear()
    maxdst.clear()

    dataline = file.readline()
    while dataline != "":
        datatuple = dataline.strip().split()
        xdst.append(float(datatuple[0]))
        mindst.append(float(datatuple[1]))
        maxdst.append(float(datatuple[2]))
        dataline = file.readline()


def interactive_simple():
    tmp = fast_inputs.param_input(
        int,
        "1<=n<=2",
        custom_prompt="По какому параметру хотите сравнивать данные?\n"
        "1 - Оптимизация\n"
        "2 - Способ индексации\n"
        "> ",
    )

    opt = ""
    indexation = ""

    if tmp == 1:
        tmp = fast_inputs.param_input(
            int,
            "1<=n<=3",
            custom_prompt="Введите желаемый способ индексации\n"
            "1 - Квадратные скобки ( a[i] )\n"
            "2 - Указатель на элемент ( *pcur )\n"
            "3 - Указатель на начало со сдвигом ( *pstart + i )\n"
            "> ",
        )
        indexation = ADRESS_FILENAME_DICT[tmp]
    else:
        tmp = fast_inputs.param_input(
            int,
            "1<=n<=2",
            custom_prompt="Какой уровень оптимизации рассматривать?\n"
            "1 - O0\n"
            "2 - O2\n"
            "> ",
        )
        opt = OPTIMIZATION_FILENAME_DICT[tmp]

    tmp = fast_inputs.param_input(
        int,
        "0<=n<=1",
        custom_prompt="Хотите поработать с данными о сортировке cлучайных массивов?\n"
        "1 - Да\n"
        "0 - Нет\n"
        "> ",
    )
    issorted = SORTED_FILENAME_DICT[tmp]

    plt.cla()

    markers = MARKERS.copy()

    for filename in os.listdir(PREPROC_DATA_DIR):
        if (
            "avg" in filename
            and opt in filename
            and issorted in filename
            and indexation in filename
        ):
            x_values = []
            y_values = []

            with open(
                os.path.join(PREPROC_DATA_DIR, filename), "r", encoding="utf-8"
            ) as f:
                parse_avg(x_values, y_values, f)

            sort_paired(x_values, y_values)

            plt.plot(
                x_values,
                y_values,
                label=filename,
                marker=markers.pop(randint(0, len(markers) - 1)),
            )

    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (мс)")
    plt.show()


def interactive_error():
    tmp = fast_inputs.param_input(
        int,
        "1<=n<=2",
        custom_prompt="По какому параметру хотите сравнивать данные?\n"
        "1 - Оптимизация\n"
        "2 - Способ индексации\n"
        "> ",
    )

    opt = ""
    indexation = ""

    if tmp == 1:
        tmp = fast_inputs.param_input(
            int,
            "1<=n<=3",
            custom_prompt="Введите желаемый способ индексации\n"
            "1 - Квадратные скобки ( a[i] )\n"
            "2 - Указатель на элемент ( *pcur )\n"
            "3 - Указатель на начало со сдвигом ( *pstart + i )\n"
            "> ",
        )
        indexation = ADRESS_FILENAME_DICT[tmp]
    else:
        tmp = fast_inputs.param_input(
            int,
            "1<=n<=2",
            custom_prompt="Какой уровень оптимизации рассматривать?\n"
            "1 - O0\n"
            "2 - O2\n"
            "> ",
        )
        opt = OPTIMIZATION_FILENAME_DICT[tmp]

    tmp = fast_inputs.param_input(
        int,
        "0<=n<=1",
        custom_prompt="Хотите поработать с данными о сортировке cлучайных массивов?\n"
        "1 - Да\n"
        "0 - Нет\n"
        "> ",
    )
    issorted = SORTED_FILENAME_DICT[tmp]

    plt.cla()

    markers = MARKERS.copy()
    colors = COLORS.copy()

    for filename in os.listdir(PREPROC_DATA_DIR):
        if (
            "avg" in filename
            and opt in filename
            and issorted in filename
            and indexation in filename
        ):
            x_values = []
            y_values = []

            with open(
                os.path.join(PREPROC_DATA_DIR, filename), "r", encoding="utf-8"
            ) as f:
                parse_avg(x_values, y_values, f)

            sort_paired(x_values, y_values)

            color = colors.pop()

            plt.plot(
                x_values,
                y_values,
                label=filename,
                marker=markers.pop(randint(0, len(markers) - 1)),
                color=color,
            )

            xerr = []
            mins = []
            maxs = []
            with open(
                os.path.join(PREPROC_DATA_DIR, filename.replace("avg", "errors")),
                "r",
                encoding="utf-8",
            ) as f:
                parse_error(xerr, mins, maxs, f)

            sort_connected(xerr, mins, maxs)

            for i in range(len(xerr)):
                mins[i] = abs(y_values[i] - mins[i])
                maxs[i] = abs(maxs[i] - y_values[i])

            plt.errorbar(x_values, y_values, [mins, maxs], color=color, capsize=3)

    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (мс)")
    plt.show()


def interactive_box():
    opt = ""
    indexation = ""

    tmp = fast_inputs.param_input(
        int,
        "1<=n<=3",
        custom_prompt="Введите желаемый способ индексации\n"
        "1 - Квадратные скобки ( a[i] )\n"
        "2 - Указатель на элемент ( *pcur )\n"
        "3 - Указатель на начало со сдвигом ( *pstart + i )\n"
        "> ",
    )

    indexation = ADRESS_FILENAME_DICT[tmp]
    tmp = fast_inputs.param_input(
        int,
        "1<=n<=2",
        custom_prompt="Какой уровень оптимизации рассматривать?\n"
        "1 - O0\n"
        "2 - O2\n"
        "> ",
    )
    opt = OPTIMIZATION_FILENAME_DICT[tmp]

    tmp = fast_inputs.param_input(
        int,
        "0<=n<=1",
        custom_prompt="Хотите поработать с данными о сортировке cлучайных массивов?\n"
        "1 - Да\n"
        "0 - Нет\n"
        "> ",
    )
    issorted = SORTED_FILENAME_DICT[tmp]

    plt.cla()

    markers = MARKERS.copy()
    colors = COLORS.copy()

    for filename in os.listdir(PREPROC_DATA_DIR):
        if (
            "avg" in filename
            and opt in filename
            and issorted in filename
            and indexation in filename
        ):
            x_values = []
            y_values = []

            with open(
                os.path.join(PREPROC_DATA_DIR, filename), "r", encoding="utf-8"
            ) as f:
                parse_avg(x_values, y_values, f)

            sort_paired(x_values, y_values)

            color = colors.pop()

            plt.plot(
                x_values,
                y_values,
                label=filename,
                marker=markers.pop(randint(0, len(markers) - 1)),
                color=color,
            )

            xerr = []
            mins = []
            maxs = []
            with open(
                os.path.join(PREPROC_DATA_DIR, filename.replace("avg", "errors")),
                "r",
                encoding="utf-8",
            ) as f:
                parse_error(xerr, mins, maxs, f)

            sort_connected(xerr, mins, maxs)

            for i in range(len(xerr)):
                mins[i] = abs(y_values[i] - mins[i])
                maxs[i] = abs(maxs[i] - y_values[i])

            plt.errorbar(x_values, y_values, [mins, maxs], color=color, capsize=3)

            with open(
                os.path.join(DATA_DIR, filename.replace("avg_", "")),
                "r",
                encoding="utf-8",
            ) as f:
                x_values = []
                y_dict = {}
                parse_to_dict(x_values, y_dict, f)

                plt.boxplot(
                    y_dict.values(),
                    positions=list(map(int, y_dict.keys())),
                    showfliers=False,
                    showmeans=False,
                    showcaps=True,
                    widths=100,
                    capwidths=70,
                    meanline=False,
                    whis=0,
                )

    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (мс)")
    plt.xticks(rotation=-45)
    plt.show()


def main():
    modenum = fast_inputs.param_input(
        int,
        "1<=n<=3",
        custom_prompt="В каком режиме строить график?\n"
        "1 - Обычный кусочно-линейный график\n"
        "2 - График с ошибкой\n"
        "3 - График с усами\n"
        "> ",
    )

    if modenum == 1:
        interactive_simple()
    elif modenum == 2:
        interactive_error()
    else:
        interactive_box()


if __name__ == "__main__":
    main()
