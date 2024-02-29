data_list = []

with open("./input.txt") as file:
    lines = file.read()
    s, instructions = lines.split("\n\n")

    for line in s.splitlines():
        linedata_list = []
        for x in range((len(line) // 4) + 1):
            linedata_list.append(line[x * 4 + 1])  # 1,5,9...

        data_list.append(linedata_list)


data_list.pop()  # pop the line with 1,2,3

# before = [[], [], [] ]
# after = [] , [], []
stack = zip(*data_list)


stack = [[char for char in i if char != " "] for i in list(stack)]

# if not reversed, top char will be in bottom
# we want it on top
stack = [list(reversed(i)) for i in stack]


# each word is an item in list
instr_list = [i.split(" ") for i in instructions.splitlines()]


for i in instr_list:
    length, source, destination = i[1], i[3], i[5]
    print(length, source, destination)

    for x in range(int(length)):
        item = stack[int(source) - 1].pop()
        stack[int(destination) - 1].append(item)

top_stack = ""
for i in stack:
    top_stack += i.pop()

print(top_stack)
