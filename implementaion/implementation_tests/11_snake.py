n = int(input())
k = int(input())

apple = []
for i in range(k):
    apple.append(list(map(int, input().split())))

L = int(input())

move = []
for i in range(L):
    move.append(list(map(str, input().split())))

dir_row = [0, -1, 0, 1]  # east, north, west, south
dir_col = [1, 0, -1, 0]
start_r = 0
ro_list = [0]


def rotate(movement):
    for rot in movement:
        if rot[1] == 'L':
            global start_r
            if start_r == 3:
                start_r = 0
                ro_list.append(start_r)
            else:
                start_r += 1
                ro_list.append(start_r)
        elif rot[1] == 'D':
            if start_r == 0:
                start_r = 3
                ro_list.append(start_r)
            else:
                start_r -= 1
                ro_list.append(start_r)


rotate(move)

pos_head = [[1, 1]]
pos_tail = [[]]
for i in move:
    i[0] = int(i[0])
for i in move[1:]:
    i[0] -= move[0][0]

count = 0
try:
    for i in range(len(move)):
        for j in range(move[i][0] - count):
            pos_tail.append(pos_head[0])
            pos_head[0][0] += dir_row[ro_list[i]]
            pos_head[0][1] += dir_col[ro_list[i]]
            print(pos_head)
            count += 1
            if any(pos_head[0] == a for a in apple):
                pass
            else:
                pos_tail.pop(0)
            if pos_head[0][0] > n or pos_head[0][1] > n or pos_head[0][0] < 1 or pos_head[0][1] < 1:
                print(count)
                raise StopIteration
except StopIteration: pass







