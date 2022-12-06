def get_processed_char_count(chars):
    with open("inputs/problem-6.txt") as file:
        content = file.readlines()[0]

    for index, _ in enumerate(content):
        four_chars = content[index:index + chars]
        if len(four_chars) == chars:
            unique_chars = list(dict.fromkeys(four_chars))

            if len(unique_chars) == chars:
                print(unique_chars)
                print(index + chars)
                return index + chars


def problem_1():
    get_processed_char_count(4)


def problem_2():
    get_processed_char_count(14)


def main():
    problem_1()
    problem_2()


if __name__ == "__main__":
    main()

# 1566
# 2265
