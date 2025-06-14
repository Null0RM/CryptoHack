from Crypto.Util.number import inverse

def CRT(ai, ni):
    M = 1
    for i in ni:
        M *= i

    x = 0
    for i in range(len(ni)):
        x += (M // ni[i]) * inverse((M // ni[i]), ni[i]) * ai[i]

    return x % M

_ai = [2, 3, 5]
_ni = [5, 11, 17]

print(CRT(_ai, _ni))
# 872