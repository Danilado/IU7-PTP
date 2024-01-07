def main():
    count = int(input())
    with open(f"./input_data/ordered_{count}.txt", "w", encoding="utf-8") as f:
        f.write(f"{count}\n")
        for i in range(count):
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
