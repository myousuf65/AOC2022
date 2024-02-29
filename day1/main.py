with open('./input.txt') as file:
    _lines = file.read()
    # lines = _lines.split('\n')

calorieCount = []
for item in _lines.split('\n\n'):
    l = item.splitlines()
    calorieCount.append(l)

# print(calorieCount)


calsum = []
for item in calorieCount:
    i = [int(i) for i in item]
    calsum.append(sum(i))



# will sort in ascending order
calsum = sorted(calsum)
#convert to decending order
# reversed will make it into class
# list wrapper change back to list
calsum = list(reversed(calsum))

# print(calsum)
print(calsum[0]+calsum[1]+calsum[2])



