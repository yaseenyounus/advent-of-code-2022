def num_list_generator(num1, num2):
    num_list = []
    for x in range(num1, num2 + 1):
        num_list.append(x)
    return num_list


def problem_1():
    fully_contained = 0

    with open("problem-4.txt") as file:
        for line in file:
            line = line.strip().split(',')
            first, second = line[0], line[1]

            first_num1, first_num2 = first.split('-')
            second_num1, second_num2 = second.split('-')

            first_num_list = num_list_generator(
                int(first_num1), int(first_num2))
            second_num_list = num_list_generator(
                int(second_num1), int(second_num2))

            print(f"{first_num_list}\n{second_num_list}")

            if set(first_num_list).issubset(second_num_list):
                print("Found in second!")
                fully_contained += 1
            elif set(second_num_list).issubset(first_num_list):
                print("Found in first!")
                fully_contained += 1

            print(f"Fully Contained: {fully_contained}\n")


def problem_2():
    overlap = 0

    with open("problem-4.txt") as file:
        for line in file:
            line = line.strip().split(',')
            first, second = line[0], line[1]

            first_num1, first_num2 = first.split('-')
            second_num1, second_num2 = second.split('-')

            first_num_list = num_list_generator(
                int(first_num1), int(first_num2))
            second_num_list = num_list_generator(
                int(second_num1), int(second_num2))

            print(f"{first_num_list}\n{second_num_list}")

            if set(first_num_list).intersection(second_num_list):
                print("Intersection!")
                overlap += 1
            elif set(second_num_list).intersection(first_num_list):
                print("Intersection!")
                overlap += 1

            print(f"Overlap: {overlap}\n")


def main():
    # problem_1()
    problem_2()


if __name__ == "__main__":
    main()
