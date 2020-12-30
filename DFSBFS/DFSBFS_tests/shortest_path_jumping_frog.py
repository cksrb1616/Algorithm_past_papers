m = list(map(int,input().split()))
n = len(m)
########
# m = [4,1,2,3,1,0,5]
# n = 7
connection = [[]*i for i in range(n)]

for i in range(n):
    if i == 0:
        #show connected index
        connection[i].append(i+m[i])
        #connection[i].append((i,m[i+m[i]]))
    if i != 0 and i+m[i]<=(n-1):
        connection[i].append(i+m[i])
    if i != 0 and i-m[i]>=0:
        connection[i].append(i-m[i])

def dfs_paths(connection, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        k, path = stack.pop()
        if k == goal:
            result.append(path)
        else:
            for m in set(connection[k]) - set(path):
                stack.append((m, path + [m]))
    return result

paths = dfs_paths(connection,0,n-1)
shortest = min(paths, key=len)
answer = len(shortest)-1
print(answer)
