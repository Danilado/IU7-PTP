from random import randint


def main():
    count = int(input())
    with open(f"./input_data/random_{count}.txt", "w", encoding="utf-8") as f:
        f.write(f"{count}\n")
        for _ in range(count):
            f.write(f"{randint(-count, count)}\n")


if __name__ == "__main__":
    main()
