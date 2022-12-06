def problem_1():
    letter_stacks = []

    with open("problem-5.txt") as file:
        content = file.readlines()

    crates = content[:8]
    instructions = content[10:]

    for index, x in enumerate(instructions):
        x = x.split()
        instructions[index] = [x[1], x[3], x[5]]

    for x in crates:
        letter_stacks.append([x[1], x[5], x[9], x[13],
                             x[17], x[21], x[25], x[29], x[33]])

    # 1 5 9 13 17 21 25 29 33

    stacks = list(zip(
        letter_stacks[0], letter_stacks[1],
        letter_stacks[2], letter_stacks[3],
        letter_stacks[4], letter_stacks[5],
        letter_stacks[6], letter_stacks[7]
    ))

    letter_stacks = []

    stack_str = ""
    for x in stacks:
        for y in x:
            stack_str += y
        letter_stacks.append(list(stack_str[::-1].strip()))
        stack_str = ""

    selected = []

    for x in instructions:
        move, origin, dest = x[0], int(x[1]) - 1, int(x[2]) - 1

        for y in range(int(move)):
            popped = letter_stacks[origin].pop()

            letter_stacks[dest].append(str(popped))

    print(letter_stacks)

    top_of_stacks = ""
    for x in letter_stacks:
        top_of_stacks += x[-1]
    print(top_of_stacks)


def problem_2():
    letter_stacks = []

    with open("problem-5.txt") as file:
        content = file.readlines()

    crates = content[:8]
    instructions = content[10:]

    for index, x in enumerate(instructions):
        x = x.split()
        instructions[index] = [x[1], x[3], x[5]]

    for x in crates:
        letter_stacks.append([x[1], x[5], x[9], x[13],
                             x[17], x[21], x[25], x[29], x[33]])

    # 1 5 9 13 17 21 25 29 33

    stacks = list(zip(
        letter_stacks[0], letter_stacks[1],
        letter_stacks[2], letter_stacks[3],
        letter_stacks[4], letter_stacks[5],
        letter_stacks[6], letter_stacks[7]
    ))

    letter_stacks = []

    stack_str = ""
    for x in stacks:
        for y in x:
            stack_str += y
        letter_stacks.append(list(stack_str[::-1].strip()))
        stack_str = ""

    for x in instructions:
        move, origin, dest = int(x[0]), int(x[1]) - 1, int(x[2]) - 1

        print(letter_stacks[origin])

        moving = letter_stacks[origin][-move:]
        print(moving)

        del letter_stacks[origin][-move:]
        print(letter_stacks[origin])

        for x in moving:
            letter_stacks[dest].append(x)

    print(letter_stacks)

    top_of_stacks = ""
    for x in letter_stacks:
        top_of_stacks += x[-1]
    print(top_of_stacks)


def main():
    problem_1()
    # problem_2()


if __name__ == "__main__":
    main()

# TDCHVHJTG
# NGCMPJLHV
