n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: #  if currency (i-k) is possible to make
            d[j]= min(d[j], d[j-array[i]]+1) # 한 단위 이전 숫자와 비교한 뒤 이전 금액을 만들어내는 방법에 현재 금액을 더하여 만들어질
                                             # 방법으로 카운트를 하나 올려주는 방식
                                             # 1 2 3 4 5 6 (2, 3, 4)
                                             # 0 1 0 2 0 3
                                             # 0 1 1 2 2(1+1) 2(1+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])