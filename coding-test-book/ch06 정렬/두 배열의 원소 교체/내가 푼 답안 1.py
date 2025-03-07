import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < a[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))