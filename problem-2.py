# rock paper
# paper rock

# rock scissors
# scissors rock

# paper scissors
# scissors paper

# rock rock
# paper paper
# scissors scissors

# A - opponent rock
# B - opponent paper
# C - opponent scissors

# Part 2
# X means lose
# Y means draw
# Z means win

X = 1  # rock
Y = 2  # paper
Z = 3  # scissors

win = 6
draw = 3
lose = 0


def main():

    score = 0

    # Part 1
    with open("problem-2.txt") as file:
        for line in file:
            print(line.split())
            opponent, me = line.split()[0], line.split()[1]

            print(opponent, me)

            if opponent == "A" and me == "Y":
                print("inside a y")

                score += Y + win
                print(score)

            elif opponent == "B" and me == "X":
                print("inside b x")

                score += X + lose
                print(score)

            elif opponent == "A" and me == "Z":
                print("inside a z")

                score += Z + lose
            elif opponent == "C" and me == "X":
                print("inside c x")

                score += X + win

            elif opponent == "B" and me == "Z":
                print("inside b z")

                score += Z + win
            elif opponent == "C" and me == "Y":
                print("inside c y")

                score += Y + lose

            elif opponent == "A" and me == "X":
                print("DRAW inside a x")

                score += X + draw
            elif opponent == "B" and me == "Y":
                print("DRAW inside b y")

                score += Y + draw
            elif opponent == "C" and me == "Z":
                print("DRAW inside c z")

                score += Z + draw
                print(score)

        print(score)

    # Part 2
    with open("problem-2.txt") as file:
        for line in file:
            print(line.split())
            opponent, endgoal = line.split()[0], line.split()[1]

            if endgoal == "X":  # lose
                if opponent == "A":  # rock
                    score += Z + lose  # scissors
                elif opponent == "B":  # paper
                    score += X + lose  # rock
                elif opponent == "C":  # scissors
                    score += Y + lose  # paper

            elif endgoal == "Y":  # draw
                if opponent == "A":  # rock
                    score += X + draw  # rock
                elif opponent == "B":  # paper
                    score += Y + draw  # paper
                elif opponent == "C":  # scissors
                    score += Z + draw  # scissors

            elif endgoal == "Z":  # win
                if opponent == "A":  # rock
                    score += Y + win  # paper
                elif opponent == "B":  # paper
                    score += Z + win  # scissors
                elif opponent == "C":  # scissors
                    score += X + win  # rock

    print(score)


if __name__ == "__main__":
    main()



# 10728
# 10751
# 13675
