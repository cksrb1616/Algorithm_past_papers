n = str(int(input()))
count = 0

for i in n:
    num = int(i)
    if num <= 1 or count <= 1:
        count += num
    else:
        count *= num

print(count)
