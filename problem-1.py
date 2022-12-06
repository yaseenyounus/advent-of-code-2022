def main():
    calories = []
    sum = 0

    with open("problem-1.txt") as file:
        for line in file:
            if len(line) == 1:
                print("BLANK")
                # print(sum)

                calories.append(sum)
                sum = 0
            else:
                sum += int(line)

        print(sorted(calories, reverse=True))

        print(68923 + 67023 + 64098)


if __name__ == "__main__":
    main()
