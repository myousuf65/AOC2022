moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

move_score = {"X": 1, "Y": 2, "Z": 3}

outcome = []

data = []
with open("./input.txt") as file:
    for line in file.readlines():
        data.append(line.strip("\n"))


for item in data:
    opponent, mine = item.split()

    print(moves[opponent], moves[mine])

    # draw
    if moves[opponent] == moves[mine]:
        print("draw")
        print(move_score[mine] + 3)
        outcome.append(move_score[mine] + 3)

    # win
    elif moves[opponent] == "rock" and moves[mine] == "paper":
        print(move_score[mine] + 6)
        outcome.append(move_score[mine] + 6)

    elif moves[opponent] == "rock" and moves[mine] == "scissors":
        outcome.append(move_score[mine] + 0)

    # win
    elif moves[opponent] == "scissors" and moves[mine] == "rock":
        outcome.append(move_score[mine] + 6)

    elif moves[opponent] == "scissors" and moves[mine] == "paper":
        outcome.append(move_score[mine] + 0)

    # loose
    elif moves[opponent] == "paper" and moves[mine] == "rock":
        outcome.append(move_score[mine] + 0)

    elif moves[opponent] == "paper" and moves[mine] == "scissors":
        outcome.append(move_score[mine] + 6)

print(sum(outcome))
