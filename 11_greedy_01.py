n = int(input())
each = list(map(int,input().split()))
each.sort()

result = 0
count = 0

for i in each:
    count+=1
    if count >= 1:
        result += 1
        count = 0
print(result)