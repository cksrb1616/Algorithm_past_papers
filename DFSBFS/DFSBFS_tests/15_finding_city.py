n,m,k,x = map(int,input().split())

ways = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    ways[a].append(b)

def connected_cities(waylist,startingpoint):
    connection = waylist[startingpoint]
    global k
    if k == 1:
        return connection
    else:
        k -= 1
        for i in connection:
            connected_cities(waylist,i)

print(connected_cities(ways,x))

# if k == 1:
#     result = connected_cities(ways,x)
#     for i in result:
#         print(i)
# else:
#     while k >0:
#         result = connected_cities(ways,x)
#         temp = []





