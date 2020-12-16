from collections import deque

n,m,k,x = map(int,input().split())
ways = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    ways[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_nod in ways[now]:
        if distance[next_nod] == -1: # not visited
            distance[next_nod] = distance[now] + 1
            q.append(next_nod)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
