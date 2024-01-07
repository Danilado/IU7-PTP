import matplotlib.pyplot as plt


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


def main():
    filename = "data/square_brackets_sort_O0_random.txt"
    x_values = []
    y_dict = {}
    with open(filename, "r", encoding="utf-8") as f:
        parse_to_dict(x_values, y_dict, f)

    plt.hist(y_dict[10000.0], density=True, bins=40)
    plt.show()


if __name__ == "__main__":
    main()
