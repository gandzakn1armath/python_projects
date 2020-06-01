while True:
    x = int(input("input the number\n"))
    factorials = list()
    v = 1
    if x > 100:
        break
    for j in range(1, x+1):
        v = v * j
        factorials.append(v)

    else:
        print(factorials)