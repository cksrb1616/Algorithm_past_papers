from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]: # index 1 부터 제일 뒤에서 하나 앞까 = 선수강 # no loop for empty list
        indegree[i] += 1
        graph[x].append(i) # 선수강 과목 x에 연결된 과목들이 어펜드 되기 위한 함

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, n + 1):
        print(result[i])

topology_sort()