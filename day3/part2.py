def check_char(char):
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    elif "A" <= char <= "Z":
        return ord(char) - ord("A") + 27


sets = []

with open("./input.txt") as file:
    counter = 0
    localset = []
    for line in file.readlines():
        line = line.strip("\n")

        if counter == 2:
            localset.append(line)
            sets.append(localset)
            localset = []
            counter = 0

        else:
            localset.append(line)
            counter += 1


allcommons = []
for item in sets:
    common = set(item[0]) & set(item[1]) & set(item[2])
    val = check_char(*common)
    allcommons.append(val)


""" print(allcommons) """
print(sum(allcommons))

# sum = 0
# for item in allcommons:
#     val = check_char(*item)
#     print(val)
#     sum += val

# print(sum)
