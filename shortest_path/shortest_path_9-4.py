#max N is 100 -> Floyd-warshall possible
INF = int(1e9)

n, m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if row == column:
            graph[row][column] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

for mid in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            graph[row][col] = min(graph[row][col],graph[row][mid]+graph[mid][col])

distance = graph[1][k]+graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)