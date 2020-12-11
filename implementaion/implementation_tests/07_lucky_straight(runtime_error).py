n = str(input())
left = 0

for i in n[:len(n)/2]:
    left += int(i)
for i in n[len(n)/2:]:
    left -= int(i)

if left == 0:
    print('LUCKY')
else:
    print('READY')