li = [3, 3]
target = 6


def check(li, target):
    for i, n in enumerate(li):
        for j, c in enumerate(li):
            if i == j:
                break
            else:
                if int(n)+int(c) == target:
                    return [j, i]
                else:
                    pass


print(check(li, target))
