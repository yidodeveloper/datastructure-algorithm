# 1: 1번 + 0 1개 1
# 2~7: 1번 + 1번 6개 1 + 6
# 8~19: 1번 + 2번 12개 1 + 6 + 12
# 20~37: 1번 + 3번 18개 1 + 6 + 12 + 18
# 38~61: 1번 + 4번 24개 1 + 6 + 12 + 18 + 24

N = int(input())
sum = 1

for i in range(N):
    sum += i * 6
    if N <= sum:
        print(1 + i)
        break