n = int(input())
scare = list(map(int,input().split()))

scare.sort()
count = 0

while scare:
    i = scare[0]
    if len(scare[:i]) == max(scare[:i]):
        count += 1
    scare = scare[i:]

print(count)
