n = input()
result = 0

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        result+=1
if n[0] == n[len(n)-1]:
    print(result//2)
else:
    print(result//2+1)
