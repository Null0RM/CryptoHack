# 정수론 지식 이용해서 수기로 p를 구할 수 있음
p = 209 * 6  - 335

for x in range(100, 1000):
    if 4 * x % p == 836:
        print(p,x)

# crypto{919, 209}