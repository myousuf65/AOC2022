x = str(121)
leftpointer = 0
rightpointer = len(x)-1
counter = len(x) // 2

while counter > 0:
    if x[leftpointer] == x[rightpointer]:
        counter -= 1
    else:
        print("not")
