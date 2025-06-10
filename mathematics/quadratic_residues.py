p = 29
ints = [14, 6, 11]

for i in ints:
    for j in range(1, p):
        res = pow(j, 2, p)
        if (res == i):
            print(i, j)
            break

# 8, 21