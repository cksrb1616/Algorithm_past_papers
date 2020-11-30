INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if row == column:
            graph[row][column] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost

for mid in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            graph[row][col] = min(graph[row][col],graph[row][mid]+graph[mid][col])

for row in range(1, n + 1):
    for col in range(1, n+1):
        if graph[row][col] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[row][col],end = ' ')
    print()
