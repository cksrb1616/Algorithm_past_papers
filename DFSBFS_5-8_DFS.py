def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            #2,3,8 에 따라 1,7로 넘어가면 7만 visited가 false라서 그 친구만 다음 dfs로 넘김
            dfs(graph, i , visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited =[False]*9
dfs(graph, 1, visited)