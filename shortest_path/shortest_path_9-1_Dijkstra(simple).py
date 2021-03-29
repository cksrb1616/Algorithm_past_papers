import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] *(n+1)

for _ in range(m):
    start,end,cost = map(int, input().split())
    graph[start].append((end,cost))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i]< min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index
def dijkstar(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1): #except the start node, n-1 nodes loop
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstar(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])

