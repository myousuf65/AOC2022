ans = 0
with open("./input.txt") as file:
    for line in file.readlines():
        first, second = line.split(",")

        s1, e1 = first.split("-")
        s2, e2 = second.split("-")

        # create list >> make int >> unpack
        s1, s2, e1, e2 = [int(x) for x in [s1, s2, e1, e2]]
        print(s1, s2, e1, e2)

        # notion notes
        if s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2:
            ans += 1

print(ans)
