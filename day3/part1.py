charDict = {}


def check_char(char):
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    elif "A" <= char <= "Z":
        return ord(char) - ord("A") + 27


allcommons = []

with open("./input.txt") as file:
    for line in file.readlines():
        halfpoint: int = len(line) // 2

        firsthalf = line[:halfpoint]
        secondhalf = line[halfpoint:]

        common: set = set(firsthalf) & set(secondhalf)
        allcommons.append(common)


sum = 0
for item in allcommons:
    val = check_char(*item)
    print(val)
    sum += val

print(sum)
