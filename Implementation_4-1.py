import time
n = int(input())
data = list(map(str, input().split()))

col_po = 1
row_po = 1

maxnumber = n
start_time = time.time()
for i in data:
    if i == 'R' and col_po<n:
        col_po+=1
    elif i =='L' and col_po>1:
        col_po-=1
    elif i =='U' and row_po>1:
        row_po-=1
    elif i=='D' and row_po<n:
        row_po+=1
    else:
        pass
print(row_po, col_po)
end_time = time.time()
print(end_time-start_time)


n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
start_time = time.time()
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <1 or ny < 1 or nx >n or ny>n:
        continue#pass는 루프의 다음 행으로 진행시키지만, continue는 루프 처음으로 돌아
    x, y = nx, ny

print(x, y)
end_time = time.time()
print(end_time-start_time)