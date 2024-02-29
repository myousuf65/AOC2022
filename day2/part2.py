moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

# a -rock
# b- paper
# c - scissors
move_score = {"A": 1, "B": 2, "C": 3}

outcome = []

data = []
with open("./input.txt") as file:
    for line in file.readlines():
        data.append(line.strip("\n"))


for item in data:
    opponent, mine = item.split()

    # draw
    if moves[mine] == "draw":
        if moves[opponent] == "rock":
            outcome.append(move_score[opponent] + 3)

        if moves[opponent] == "paper":
            outcome.append(move_score[opponent] + 3)

        if moves[opponent] == "scissors":
            outcome.append(move_score[opponent] + 3)

    elif moves[mine] == "win":
        if moves[opponent] == "rock":
            outcome.append(move_score["B"] + 6)

        if moves[opponent] == "paper":
            outcome.append(move_score["C"] + 6)

        if moves[opponent] == "scissors":
            outcome.append(move_score["A"] + 6)

    elif moves[mine] == "lose":
        if moves[opponent] == "rock":
            outcome.append(move_score["C"] + 0)

        if moves[opponent] == "paper":
            outcome.append(move_score["A"] + 0)

        if moves[opponent] == "scissors":
            outcome.append(move_score["B"] + 0)


print(sum(outcome))
