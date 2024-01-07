import os
import statistics

DATADIR = "./data"
OUTDIR = "./preproc_data"


def main():
    if not os.path.isdir(DATADIR):
        print("Константа DATADIR задана неверно")
        return
    if not os.path.isdir(OUTDIR):
        print("Константа OUTDIR задана неверно")
        return

    for filename in os.listdir(DATADIR):
        if not ".txt" in filename:
            continue
        filepath = os.path.join(DATADIR, filename)

        data = {}
        avgs = {}
        errors = {}
        keys = []

        with open(filepath, "r", encoding="utf-8") as datafile:
            dataline = datafile.readline()

            while dataline != "":
                datapair = dataline.strip().split()
                key = datapair[0]
                if key not in keys:
                    keys.append(key)

                value = int(datapair[1])

                if not key in data:
                    data[key] = []
                data[key].append(value)

                if not key in avgs:
                    avgs[key] = value
                else:
                    avgs[key] = (avgs[key] + value) / 2

                if not key in errors:
                    errors[key] = [value, value]
                else:
                    errors[key][0] = min(value, errors[key][0])
                    errors[key][1] = max(value, errors[key][1])

                dataline = datafile.readline()

        with open(f"{OUTDIR}/avg_{filename}", mode="w", encoding="utf-8") as f:
            for key in keys:
                f.write(f"{key} {avgs[key]:.8g}\n")

        with open(f"{OUTDIR}/errors_{filename}", mode="w", encoding="utf-8") as f:
            for key in keys:
                f.write(f"{key} {errors[key][0]:.8g} {errors[key][1]:.8g}\n")

        with open(f"{OUTDIR}/quantiles_{filename}", mode="w", encoding="utf-8") as f:
            for key in keys:
                quantiles = statistics.quantiles(data[key])
                f.write(
                    f"{key} {quantiles[0]:.8g} {quantiles[1]:.8g} {quantiles[2]:.8g}\n"
                )


if __name__ == "__main__":
    main()
