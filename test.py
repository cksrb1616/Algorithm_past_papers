data = list(map(int, input().split()))
print(data[1:-1])
print(data[0])
graph = [[] for i in range(3 + 1)]

for x in data[1:-1]:  # index 1 부터 제일 뒤에서 하나 앞까 = 선수강의
    graph[x].append(1)
print(graph)