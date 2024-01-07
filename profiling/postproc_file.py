from random import randint
import matplotlib.pyplot as plt
import os

MARKERS = ["D", "h", "+", "x", "*", "s", "1", "^", "."]
COLORS = ["r", "g", "b", "c", "m", "y"]


DATA_DIR = "../data"
PREPROC_DATA_DIR = "./"
POSTPROC_DATA_DIR = "../postproc_svg"


def sort_paired(src, pair):
    for i in range(len(src) - 1):
        for j in range(len(src) - 1 - i):
            if src[j] > src[j + 1]:
                src[j], src[j + 1] = src[j + 1], src[j]
                pair[j], pair[j + 1] = pair[j + 1], pair[j]


def parse_avg(dstx, dsty, file):
    dstx.clear()
    dsty.clear()

    dataline = file.readline()
    while dataline != "":
        datapair = dataline.strip().split()
        dstx.append(float(datapair[0]))
        dsty.append(float(datapair[1]))
        dataline = file.readline()


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


def sort_connected(src, a1, a2):
    for i in range(len(src) - 1):
        for j in range(len(src) - 1 - i):
            if src[j] > src[j + 1]:
                src[j], src[j + 1] = src[j + 1], src[j]
                a1[j], a1[j + 1] = a1[j + 1], a1[j]
                a2[j], a2[j + 1] = a2[j + 1], a2[j]


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


def simple_graph(rnd: bool, out_file):
    plt.rcParams["figure.figsize"] = [16.00, 9.0]
    plt.rcParams["figure.autolayout"] = True

    checker = "random" if rnd else "ordered"

    x_values = []
    y_values = []

    markers = MARKERS.copy()

    for filename in os.listdir(PREPROC_DATA_DIR):
        if "avg" in filename and checker in filename:
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

    plt.gca().set_position([0, 0, 1, 1])
    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (нс)")
    plt.savefig(out_file)


def error_graph(_, out_file):
    plt.rcParams["figure.figsize"] = [16.00, 9.0]
    plt.rcParams["figure.autolayout"] = True

    markers = MARKERS.copy()
    colors = COLORS.copy()

    for filename in os.listdir(PREPROC_DATA_DIR):
        if "avg" in filename and "O2" in filename and "random" in filename:
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

    plt.gca().set_position([0, 0, 1, 1])
    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (нс)")
    plt.savefig(out_file)


def moustache_graph(in_file, out_file):
    plt.rcParams["figure.figsize"] = [16.00, 9.0]
    plt.rcParams["figure.autolayout"] = True

    markers = MARKERS.copy()
    colors = COLORS.copy()

    x_values = []
    y_values = []

    with open(os.path.join(f"avg_{in_file}.txt"), "r", encoding="utf-8") as f:
        parse_avg(x_values, y_values, f)

    sort_paired(x_values, y_values)

    color = colors.pop()

    plt.plot(
        x_values,
        y_values,
        label=in_file,
        marker=markers.pop(randint(0, len(markers) - 1)),
        color=color,
    )

    xerr = []
    mins = []
    maxs = []
    with open(
        f"errors_{in_file}.txt",
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
        f"../data/{in_file}.txt",
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

    plt.gca().set_position([0, 0, 1, 1])
    plt.legend()
    plt.xlabel("Количество элементов")
    plt.ylabel("Время выполнения (нс)")
    plt.xticks(rotation=-45)
    plt.savefig(out_file)


def main():
    type = int(input())
    arg1 = input()
    out_file = input()

    if type == 1:
        simple_graph(bool(arg1), out_file)
    elif type == 2:
        error_graph(arg1, out_file)
    else:
        moustache_graph(arg1, out_file)


if __name__ == "__main__":
    main()
