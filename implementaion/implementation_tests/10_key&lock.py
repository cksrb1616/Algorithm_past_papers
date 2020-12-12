def solution(key, lock):

    answer = True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
alock = []
bkey = []
n = len(key)

for i in range(3):
    for j in range(3):
        if lock[i][j] == 0:
            n, m = i, j
            alock.append([n, m])
        if key[i][j] == 1:
            n, m = i, j
            bkey.append([n, m])
# #rotation
# for i in bkey:
#     if i[0] == n-1:
#         i[0]= i[1]
#         i[1] = 0
#     else:
#         new_col = -1*(i[0]-(n-1))
#         i[0] = i[1]
#         i[1] = new_col

# new position value with base postition
base = [[1, 1]]
base[0][0] = alock[0][0]
base[0][1] = alock[0][1]
for i in alock:
    i[0] = i[0] - base[0][0]
    i[1] = i[1] - base[0][1]

# remaining = list(filter(lambda i: i not in alock, bkey))
# for i in remaining:
#     if i[0][0] + base[0][0] > (n-1) or i[0][0] + base[0][0] < 0:
#         if i[0][1] + base[0][1] > (n-1) or i[0][1] + base[0][1] < 0:
#             answer = True
