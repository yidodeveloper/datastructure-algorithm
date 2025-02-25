import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
counts = []

def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            counts.append(count)
            count = 0

print(result)

counts.sort()
for i in counts:
    print(i)