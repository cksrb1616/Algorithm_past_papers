n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
#a = sorted(a,reverse=True)

for i in a:
    print(i, end=' ')
