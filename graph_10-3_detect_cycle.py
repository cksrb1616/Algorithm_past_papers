def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] # found parent[x] is returned

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

p, e = map(int, input().split())
parent = [0] * (p + 1)

for i in range(1, p + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int,input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('cycle')
else:
    print('no cycle')