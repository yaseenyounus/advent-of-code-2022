import string

common_char = []
letters = []

for x in string.ascii_letters:
    letters.append(x)


def problem_1():
    sum = 0

    with open("problem-3.txt") as file:
        for line in file:
            line = line.strip()

            first_half, second_half = line[0:len(
                line) // 2], line[len(line) // 2:]

            print(first_half, second_half)

            common_char.append(
                list(set(first_half).intersection(second_half))[0])

    print(common_char)
    for x in common_char:
        print(letters.index(x) + 1)
        sum += (letters.index(x) + 1)

    print(sum)


def problem_2():
    sum = 0

    with open("problem-3.txt") as file:
        file_list = file.readlines()

    for index, x in enumerate(file_list):
        file_list[index] = x.replace('\n', '')

    print(file_list)

    print(file_list[::3])
    every_third = file_list[::3]

    for x in every_third:
        print(file_list.index(x))
        first = file_list[file_list.index(x)]
        second = file_list[file_list.index(x) + 1]
        third = file_list[file_list.index(x) + 2]
        print(first, second, third)

        print(list(set(first).intersection(second, third))[0])
        common_char.append(list(set(first).intersection(second, third))[0])

    print(common_char)
    for x in common_char:
        print(letters.index(x) + 1)
        sum += (letters.index(x) + 1)

    print(sum)


def main():
    # problem_1()
    problem_2()


if __name__ == "__main__":
    main()
